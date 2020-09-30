import unittest
from hw4 import printRepos

class TestHW4(unittest.TestCase):
    def testGitUser(self):
        self.assertEqual(printRepos("3"),['Repo: dotfiles Number of commits: 12', 'Repo: pair-box Number of commits: 7'],'Fail')
    def testNonUser(self):
        self.assertEqual(printRepos('ewibu3inf834nfeqop3909nwo'),'User Does not Exist','Fail')
    def testNonString(self):
        self.assertEqual(printRepos(273648732),'Not a String','Fail')



if __name__ == '__main__':
    unittest.main(exit=False)
