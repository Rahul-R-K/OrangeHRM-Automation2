import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from BaseClass import BaseClass
from LoginPage import HomePage
#from AdminPage import AdminPage
#from MenuPage import MenuPage

class Testcase1(BaseClass):
    def test_TC_PIM_01(self):
        try:
            self.verifythePresence("username")
            username = HomePage(self.driver)
            username.enterUserName().send_keys("Admin")
            Forgotpassword = HomePage(self.driver)
            Forgotpassword.ClickForgotPassword().click()
            time.sleep(2)
            enterusername = HomePage(self.driver)
            enterusername.enterConfromUserName().send_keys("Admin")
            Submit = HomePage(self.driver)
            Submit.enterSubmit().click()
        except Exception as e:
            print(f"Caught exception: {type(e).__name__}: {e}")

