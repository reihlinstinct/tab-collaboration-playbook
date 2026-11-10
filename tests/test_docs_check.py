import importlib.util
from pathlib import Path
import subprocess
import tempfile
import unittest

REPO = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location('check', REPO / 'scripts/check_docs.py')
CHECK = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CHECK)

# Synthetic language codes only. Real codes come from the docs folders, never
# from this file (the hardcoded-language scan below would flag them).
DOC = '# Title\n\nSee [sources](../sources.md).\n\n## Part\n\nText.\n'


def block(code, name='Name', direction='ltr', draft='no'):
    return ('<!-- language\ncode: ' + code + '\nname: ' + name + '\ndir: ' + direction
            + '\nmachine_draft: ' + draft + '\n-->\n# ' + name + '\n')


def fixture(languages, docs=('setup.md', 'workflow.md'), readme=None):
    """Return {path: text} for a minimal valid repository in the given languages."""
    files = {name: 'safe example\n' for name in
             ['CONTRIBUTING.md', 'SECURITY.md', 'LICENSE', 'docs/sources.md', 'docs/templates.md']}
    links = []
    for code, draft in languages:
        files['docs/' + code + '/README.md'] = block(code, draft=draft)
        links.append('[' + code + '](docs/' + code + '/README.md)')
        for doc in docs:
            text = DOC
            if draft == 'yes':
                text = CHECK.MACHINE_DRAFT_MARK + '\n' + text
            files['docs/' + code + '/' + doc] = text
            links.append('[' + code + ' ' + doc + '](docs/' + code + '/' + doc + ')')
    files['README.md'] = readme if readme is not None else '\n'.join(links) + '\n'
    return files


class Scan:
    def scan(self, name, text, files=None):
        files = dict(files or fixture([('xx', 'no'), ('yy', 'no')]))
        if name is not None:
            files[name] = text
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            subprocess.run(['git', 'init', '-q', str(root)], check=True)
            for relative, content in files.items():
                if content is None:
                    continue
                path = root / relative
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(content, encoding='utf-8')
            subprocess.run(['git', 'add', '.'], cwd=root, check=True)
            return CHECK.problems(root)


class CheckerTests(Scan, unittest.TestCase):
    def test_safe(self):
        self.assertEqual(self.scan('README.md', fixture([('xx', 'no'), ('yy', 'no')])['README.md']
                                   + 'תיעוד public safe\n'), [])

    def test_email(self):
        self.assertTrue(self.scan('docs/sources.md', 'person' + '@' + 'example.invalid'))

    def test_bad_link(self):
        self.assertTrue(self.scan('docs/sources.md', '[missing](missing.md)'))

    def test_private_key_file(self):
        self.assertTrue(self.scan('secret.key', 'secret'))

    def test_safe_link(self):
        self.assertEqual(self.scan('docs/sources.md', '[security](../SECURITY.md)'), [])

    def test_token(self):
        self.assertTrue(self.scan('docs/sources.md', 'gh' + 'p_' + 'x' * 30))

    def test_fingerprint(self):
        self.assertTrue(self.scan('docs/sources.md', ':'.join(['AB'] * 20)))

    def test_phone(self):
        self.assertTrue(self.scan('docs/sources.md', '+' + '123456789012'))


class LanguageDiscoveryTests(unittest.TestCase):
    """Languages come only from docs/<code>/README.md language blocks."""

    def make(self, files):
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        root = Path(directory.name)
        for relative, content in files.items():
            path = root / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding='utf-8')
        return root

    def test_discovers_every_language_block(self):
        root = self.make(fixture([('xx', 'no'), ('yy', 'no'), ('zz', 'yes')]))
        self.assertEqual(sorted(CHECK.languages(root)), ['xx', 'yy', 'zz'])
        self.assertEqual(CHECK.languages(root)['zz']['machine_draft'], 'yes')

    def test_folder_without_block_is_not_a_language(self):
        files = fixture([('xx', 'no')])
        files['docs/design/001-note.md'] = '# Note\n'
        files['docs/notes/README.md'] = '# Not a language\n'
        self.assertEqual(sorted(CHECK.languages(self.make(files))), ['xx'])

    def test_new_language_needs_only_its_folder(self):
        two = fixture([('xx', 'no'), ('yy', 'no')])
        three = fixture([('xx', 'no'), ('yy', 'no'), ('zz', 'yes')])
        added = sorted(set(three) - set(two))
        self.assertTrue(all(name.startswith('docs/zz/') or name == 'README.md' for name in added))

    def test_doc_set_is_discovered_not_listed(self):
        root = self.make(fixture([('xx', 'no')], docs=('setup.md', 'workflow.md', 'extra.md')))
        self.assertEqual(CHECK.doc_names(root, CHECK.languages(root)),
                         ['extra.md', 'setup.md', 'workflow.md'])


class LanguageParityTests(Scan, unittest.TestCase):
    def base(self, **kwargs):
        return fixture([('xx', 'no'), ('yy', 'no'), ('zz', 'yes')], **kwargs)

    def test_three_languages_pass(self):
        self.assertEqual(self.scan(None, None, self.base()), [])

    def test_missing_doc_in_one_language_fails(self):
        files = self.base()
        files['README.md'] = files['README.md'].replace('[zz workflow.md](docs/zz/workflow.md)', '')
        del files['docs/zz/workflow.md']
        self.assertIn('missing translation: docs/zz/workflow.md', self.scan(None, None, files))

    def test_extra_doc_in_one_language_fails(self):
        files = self.base()
        files['docs/xx/extra.md'] = DOC
        found = self.scan(None, None, files)
        self.assertIn('missing translation: docs/yy/extra.md', found)
        self.assertIn('missing translation: docs/zz/extra.md', found)

    def test_required_doc_missing_everywhere_fails(self):
        found = self.scan(None, None, fixture([('xx', 'no'), ('yy', 'no')], docs=('setup.md',)))
        self.assertIn('missing in every language: workflow.md', found)

    def test_no_language_fails(self):
        files = self.base()
        for name in [n for n in files if n.startswith('docs/') and n.count('/') == 2]:
            del files[name]
        files['README.md'] = 'safe\n'
        self.assertIn('no language folder found under docs/', self.scan(None, None, files))

    def test_heading_outline_mismatch_fails(self):
        files = self.base()
        files['docs/zz/setup.md'] = files['docs/zz/setup.md'] + '\n## Extra\n'
        self.assertTrue(any(p.startswith('outline differs: docs/zz/setup.md')
                            for p in self.scan(None, None, files)))

    def test_link_target_mismatch_fails(self):
        files = self.base()
        files['docs/yy/setup.md'] = files['docs/yy/setup.md'].replace('../sources.md', '../templates.md')
        self.assertTrue(any(p.startswith('links differ: docs/yy/setup.md')
                            for p in self.scan(None, None, files)))

    def test_fragment_only_difference_passes(self):
        files = self.base()
        for code in ['xx', 'yy', 'zz']:
            files['docs/' + code + '/setup.md'] += '[a](workflow.md#part-' + code + ')\n'
        self.assertEqual(self.scan(None, None, files), [])

    def test_machine_draft_without_mark_fails(self):
        files = self.base()
        files['docs/zz/setup.md'] = DOC
        self.assertIn('machine draft not marked: docs/zz/setup.md', self.scan(None, None, files))

    def test_block_code_must_match_folder(self):
        files = self.base()
        files['docs/zz/README.md'] = block('qq', draft='yes')
        self.assertIn('language block code qq does not match folder docs/zz/',
                      self.scan(None, None, files))

    def test_block_fields_are_checked(self):
        files = self.base()
        files['docs/zz/README.md'] = block('zz', direction='up', draft='maybe')
        found = self.scan(None, None, files)
        self.assertIn('language block docs/zz/README.md: dir must be ltr or rtl', found)
        self.assertIn('language block docs/zz/README.md: machine_draft must be yes or no', found)

    def test_readme_must_link_every_translation(self):
        files = self.base()
        files['README.md'] = files['README.md'].replace('[zz setup.md](docs/zz/setup.md)', '')
        self.assertIn('README.md does not link docs/zz/setup.md', self.scan(None, None, files))

    def test_readme_must_link_every_language_folder(self):
        files = self.base()
        files['README.md'] = files['README.md'].replace('[zz](docs/zz/README.md)', '')
        self.assertIn('README.md does not link docs/zz/README.md', self.scan(None, None, files))


class HardcodedLanguageTests(Scan, unittest.TestCase):
    def files(self):
        return fixture([('xx', 'no'), ('yy', 'no')])

    def test_code_literal_in_python_fails(self):
        found = self.scan('scripts/tool.py', "LANGS = ['xx', 'yy']\n", self.files())
        self.assertIn('hardcoded language code xx: scripts/tool.py', found)
        self.assertIn('hardcoded language code yy: scripts/tool.py', found)

    def test_code_in_docs_path_in_python_fails(self):
        found = self.scan('tests/test_tool.py', "PATH = 'docs/xx/setup.md'\n", self.files())
        self.assertIn('hardcoded language code xx: tests/test_tool.py', found)

    def test_unrelated_python_passes(self):
        self.assertEqual(self.scan('scripts/tool.py', "NAME = 'xxl'\nother = 'axx'\n", self.files()), [])


class RepositoryTests(unittest.TestCase):
    """The real repository: every discovered language carries every doc."""

    def test_repository_passes_all_checks(self):
        self.assertEqual(CHECK.problems(REPO), [])

    def test_every_language_has_every_doc(self):
        langs = CHECK.languages(REPO)
        self.assertGreaterEqual(len(langs), 2)
        names = CHECK.doc_names(REPO, langs)
        for code in langs:
            present = sorted(p.name for p in (REPO / 'docs' / code).glob('*.md') if p.name != 'README.md')
            self.assertEqual(present, names, code)

    def test_machine_drafts_are_marked(self):
        for code, info in CHECK.languages(REPO).items():
            if info['machine_draft'] == 'yes':
                for name in CHECK.doc_names(REPO, {code: info}):
                    text = (REPO / 'docs' / code / name).read_text(encoding='utf-8')
                    self.assertIn(CHECK.MACHINE_DRAFT_MARK, text, code + '/' + name)


if __name__ == '__main__':
    unittest.main()
