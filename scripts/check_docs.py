"""Dependency-free documentation and public-data hygiene checks."""
from pathlib import Path
import re
import subprocess


def problems(root):
    found = []
    required = ['README.md', 'CONTRIBUTING.md', 'SECURITY.md', 'LICENSE',
                'docs/en/setup.md', 'docs/he/setup.md', 'docs/en/workflow.md',
                'docs/he/workflow.md', 'docs/sources.md', 'docs/templates.md']
    for name in required:
        if not (root / name).is_file():
            found.append('missing: ' + name)
    names = subprocess.check_output(['git', 'ls-files', '-z'], cwd=root).decode().split('\0')
    patterns = [r'[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}',
                r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----',
                r'gh[pousr]_[A-Za-z0-9]{20,}', r'github_pat_[A-Za-z0-9_]{20,}',
                r'(?:[A-F0-9]{2}:){15,}[A-F0-9]{2}',
                r'\+\d[\d ()-]{8,}\d']
    for name in filter(None, names):
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
