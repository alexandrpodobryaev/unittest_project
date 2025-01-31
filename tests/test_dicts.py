import unittest
from utils import dicts


class TestDicts(unittest.TestCase):

    def test_get_val(self):
        self.assertEqual(dicts.get_val({"vcs": "mercurial"}, "vcs", None), 'mercurial')
        self.assertEqual(dicts.get_val({"vcs": "mercurial"}, "vcs", "git"), 'mercurial')
        self.assertEqual(dicts.get_val({}, "vcs", "git"), 'git')
        self.assertEqual(dicts.get_val({}, "vcs", "bazaar"), 'bazaar')
