"""Dependency-free documentation and public-data hygiene checks.

Languages are discovered, never listed. A language is a folder docs/<code>/
whose README.md opens with a language block:

    <!-- language
    code: <code, equal to the folder name>
    name: <the language's own name>
    dir: ltr | rtl
    machine_draft: yes | no
    -->

Adding a language means adding that folder (its README.md plus one file per
doc) and linking it and its docs from README.md; no code or test changes.
"""
from pathlib import Path
import re
import subprocess

LANGUAGE_BLOCK = re.compile(r'\A<!-- language\n(.*?)\n-->\n', re.S)
LANGUAGE_FIELDS = ('code', 'name', 'dir', 'machine_draft')
MACHINE_DRAFT_MARK = '<!-- machine-draft: needs native review -->'
# Docs every language must carry (names only; the language list is discovered).
REQUIRED_DOCS = ['setup.md', 'workflow.md']
LINK = re.compile(r'\]\(([^ )]+)\)')


def languages(root):
    """Return {code: block fields} for every docs/<folder>/README.md language block."""
    found = {}
    docs = Path(root) / 'docs'
    if not docs.is_dir():
        return found
    for folder in sorted(path for path in docs.iterdir() if path.is_dir()):
        readme = folder / 'README.md'
        if not readme.is_file():
            continue
        match = LANGUAGE_BLOCK.match(readme.read_text(encoding='utf-8'))
        if not match:
            continue
        fields = {}
        for line in match.group(1).splitlines():
            key, _, value = line.partition(':')
            fields[key.strip()] = value.strip()
        found[folder.name] = fields
    return found


def doc_names(root, langs):
    """Return the sorted union of doc file names across the language folders."""
    names = set()
    for code in langs:
        names.update(path.name for path in (Path(root) / 'docs' / code).glob('*.md')
                      if path.name != 'README.md')
    return sorted(names)


def outline(text):
    return [len(line) - len(line.lstrip('#')) for line in text.splitlines()
            if re.match(r'#{1,6} ', line)]


def link_targets(text):
    """Link targets with in-page fragments dropped (anchors follow each language's headings)."""
    return sorted({target if '://' in target else target.split('#')[0]
                   for target in LINK.findall(text) if not target.startswith('#')})


def language_problems(root):
    found = []
    langs = languages(root)
    if not langs:
        return ['no language folder found under docs/']
    for code, fields in langs.items():
        where = 'language block docs/' + code + '/README.md: '
        for field in LANGUAGE_FIELDS:
            if not fields.get(field):
                found.append(where + 'missing ' + field)
        if fields.get('code') and fields['code'] != code:
            found.append('language block code ' + fields['code'] + ' does not match folder docs/' + code + '/')
        if fields.get('dir') not in ('ltr', 'rtl'):
            found.append(where + 'dir must be ltr or rtl')
        if fields.get('machine_draft') not in ('yes', 'no'):
            found.append(where + 'machine_draft must be yes or no')
    names = doc_names(root, langs)
    for name in REQUIRED_DOCS:
        if name not in names:
            found.append('missing in every language: ' + name)
    readme = Path(root) / 'README.md'
    index = set(link_targets(readme.read_text(encoding='utf-8'))) if readme.is_file() else set()
    codes = sorted(langs)
    for code in codes:
        if 'docs/' + code + '/README.md' not in index:
            found.append('README.md does not link docs/' + code + '/README.md')
    for name in names:
        texts = {}
        for code in codes:
            relative = 'docs/' + code + '/' + name
            path = Path(root) / relative
            if not path.is_file():
                found.append('missing translation: ' + relative)
                continue
            texts[code] = path.read_text(encoding='utf-8')
            if langs[code].get('machine_draft') == 'yes' and MACHINE_DRAFT_MARK not in texts[code]:
                found.append('machine draft not marked: ' + relative)
            if relative not in index:
                found.append('README.md does not link ' + relative)
        if not texts:
            continue
        reference = min(texts)
        for code, text in texts.items():
            other = 'docs/' + reference + '/' + name
            if outline(text) != outline(texts[reference]):
                found.append('outline differs: docs/' + code + '/' + name + ' vs ' + other)
            if link_targets(text) != link_targets(texts[reference]):
                found.append('links differ: docs/' + code + '/' + name + ' vs ' + other)
    return found


def hardcoded_language_problems(root, names):
    """Python sources must not name a discovered language code as a literal or path part."""
    found = []
    for code in sorted(languages(root)):
        pattern = re.compile("['\"/]" + re.escape(code) + "['\"/]")
        for name in names:
            if name.endswith('.py') and pattern.search((Path(root) / name).read_text(encoding='utf-8')):
                found.append('hardcoded language code ' + code + ': ' + name)
    return found


def problems(root):
    root = Path(root)
    found = []
    required = ['README.md', 'CONTRIBUTING.md', 'SECURITY.md', 'LICENSE',
                'docs/sources.md', 'docs/templates.md']
    for name in required:
        if not (root / name).is_file():
            found.append('missing: ' + name)
    found.extend(language_problems(root))
    names = [name for name in
             subprocess.check_output(['git', 'ls-files', '-z'], cwd=root).decode().split('\0') if name]
    found.extend(hardcoded_language_problems(root, names))
    patterns = [r'[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}',
                r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----',
                r'gh[pousr]_[A-Za-z0-9]{20,}', r'github_pat_[A-Za-z0-9_]{20,}',
                r'(?:[A-F0-9]{2}:){15,}[A-F0-9]{2}',
                r'\+\d[\d ()-]{8,}\d']
    for name in names:
        path = root / name
        if path.suffix.lower() in {'.p12', '.pfx', '.pem', '.key', '.eml'}:
            found.append('unsafe file type: ' + name)
            continue
        text = path.read_text(encoding='utf-8')
        for pattern in patterns:
            if re.search(pattern, text, re.I):
                found.append('private-data pattern: ' + name)
        if path.suffix == '.md':
            for target in re.findall(r'\]\(([^ )]+)\)', text):
                if '://' in target or target.startswith('#'):
                    continue
                if not (path.parent / target.split('#')[0]).exists():
                    found.append('broken local link: ' + name + ' -> ' + target)
    return found


if __name__ == '__main__':
    result = problems(Path(__file__).resolve().parents[1])
    print('\n'.join(result) if result else 'Documentation and hygiene checks passed')
    raise SystemExit(bool(result))
