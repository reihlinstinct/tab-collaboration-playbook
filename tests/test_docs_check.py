import importlib.util
from pathlib import Path
import subprocess
import tempfile
import unittest

SPEC = importlib.util.spec_from_file_location('check', Path(__file__).resolve().parents[1] / 'scripts/check_docs.py')
CHECK = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CHECK)


class CheckerTests(unittest.TestCase):
    def scan(self, name, text):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            subprocess.run(['git', 'init', '-q', str(root)], check=True)
            for required in ['README.md', 'CONTRIBUTING.md', 'SECURITY.md', 'LICENSE',
                             'docs/en/setup.md', 'docs/he/setup.md', 'docs/en/workflow.md',
                             'docs/he/workflow.md', 'docs/sources.md', 'docs/templates.md']:
                path = root / required
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text('safe example\n', encoding='utf-8')
            (root / name).write_text(text, encoding='utf-8')
            subprocess.run(['git', 'add', '.'], cwd=root, check=True)
            return CHECK.problems(root)

    def test_safe(self):
        self.assertEqual(self.scan('README.md', 'תיעוד public safe\n'), [])

    def test_email(self):
        self.assertTrue(self.scan('README.md', 'person' + '@' + 'example.invalid'))

    def test_bad_link(self):
        self.assertTrue(self.scan('README.md', '[missing](missing.md)'))

    def test_private_key_file(self):
        self.assertTrue(self.scan('secret.key', 'secret'))

    def test_safe_link(self):
        self.assertEqual(self.scan('README.md', '[security](SECURITY.md)'), [])

    def test_token(self):
        self.assertTrue(self.scan('README.md', 'gh' + 'p_' + 'x' * 30))

    def test_fingerprint(self):
        self.assertTrue(self.scan('README.md', ':'.join(['AB'] * 20)))

    def test_phone(self):
        self.assertTrue(self.scan('README.md', '+' + '123456789012'))


if __name__ == '__main__':
    unittest.main()
