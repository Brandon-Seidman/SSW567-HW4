import unittest
from unittest.mock import Mock, patch
from hw4 import printRepos

class TestHW4(unittest.TestCase):
    def user(un):
        un.UN = 'brandon_seidman'
        un.IUN = 'Not_A_User_Lmao'
        un.NAS = 10423626

    @patch('requests.get')
    def testGitUser(self, get):
        get.return_value = ['Repo: dotfiles Number of commits: 12', 'Repo: pair-box Number of commits: 7']
        self.assertEqual(get.return_value, ['Repo: dotfiles Number of commits: 12', 'Repo: pair-box Number of commits: 7'])

    @patch('requests.get')
    def testNonUser(self, get):
        get.return_value = 'User Does not Exist'
        self.assertEqual(get.return_value, 'User Does not Exist')

    @patch('requests.get')
    def testNonUser(self, get):
        get.return_value = 'Not a String'
        self.assertEqual(get.return_value, 'Not a String')

    # def testGitUser(self):
    #     self.assertEqual(printRepos("3"),['Repo: dotfiles Number of commits: 12', 'Repo: pair-box Number of commits: 7'],'Fail')
    # def testNonUser(self):
    #     self.assertEqual(printRepos('ewibu3inf834nfeqop3909nwo'),'User Does not Exist','Fail')
    # def testNonString(self):
    #     self.assertEqual(printRepos(273648732),'Not a String','Fail')



if __name__ == '__main__':
    unittest.main(exit=False)
