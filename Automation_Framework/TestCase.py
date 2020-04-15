import config
import Methods
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class TestCases:
    driver = webdriver.Chrome(ChromeDriverManager().install())
       
    def setUp(self):
        Methods.OpenURL(self.driver)
        	
    def tearDown(self):
        Methods.CloseBrowser(self.driver)
        
    def TestCase_Login(self):
        Methods.LoginToPage(self.driver)
                       
    def TestCase_Language(self):
        Methods.ChangeLanguage(self.driver)
                
    def TestCase_verifyTabs(self):
        Methods.tab_clickable(self.driver)
                
    def TestCase_ClientDetails(self):
        Methods.GotoClient(self.driver)
        
        

t=TestCases()
t.setUp()
t.TestCase_Login()
#t.TestCase_Language()
t.TestCase_verifyTabs()
t.TestCase_ClientDetails()
t.tearDown()

'''
#if __name__=="__main__":
    #unittest.main(verbosity=2)
    
    
    test_suite = unittest.TestSuite([Test_Cases])#([TestCase_Login, TestCase_Language,TestCase_verifyTabs,TestCase_ClientDetails])

    # open the report file
    outfile = open(dir + "\SeleniumPythonTestSummary.html", "w")

    # configure HTMLTestRunner options
    runner = HTMLTestRunner.HTMLTestRunner(stream=outfile,title='Test Report', description='Acceptance Tests')

    # run the suite using HTMLTestRunner
    runner.run(test_suite)
'''