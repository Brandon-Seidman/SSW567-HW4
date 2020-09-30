import unittest
from hw4 import printRepos

class TestHW4(unittest.TestCase):
    def testMyGit(self):
        self.assertEqual(printRepos('brandon-seidman'),["Repo: E115-Notes Number of commits: 7", "Repo: SSW567 Number of commits: 6", "Repo: TriangleHW2 Number of commits: 24"],'Fail')
    def testFriendsGit(self):
        self.assertEqual(printRepos('mikedelgaudio'),["Repo: behave Number of commits: 30", "Repo: BullishBayDemos Number of commits: 1", "Repo: ChatBoi.io Number of commits: 2", "Repo: COVID-19 Number of commits: 30", "Repo: CS-555-GEDCOM Number of commits: 30", "Repo: delgaudiomike.com Number of commits: 30", "Repo: delgaudiomike.com_v2 Number of commits: 30", "Repo: FTP-Deploy-Action Number of commits: 30", "Repo: git-uploader Number of commits: 6", "Repo: Linux-Server-Monitor Number of commits: 2", "Repo: Machine-Learning-Fun Number of commits: 4", "Repo: quackForHelp Number of commits: 30", "Repo: RedditCommentScraper Number of commits: 17", "Repo: resume Number of commits: 16", "Repo: rollingBallGame Number of commits: 2", "Repo: Snake-Gaming Number of commits: 8", "Repo: xCode_StrikeTeam Number of commits: 4"],'Fail')
    def testNonUser(self):
        self.assertEqual(printRepos('ewibu3inf834nfeqop3909nwo'),'User Does not Exist','Fail')
    def testNonString(self):
        self.assertEqual(printRepos(273648732),'Not a String','Fail')



if __name__ == '__main__':
    unittest.main(exit=False)
