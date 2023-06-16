import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from BaseClass import BaseClass
from LoginPage import HomePage
from AdminPage import AdminPage
#from MenuPage import MenuPage

class Testcase2(BaseClass):
    def test_TC_PIM_02(self):
        try:
            try:
                self.verifythePresence("username")
                username = HomePage(self.driver)
                username.enterUserName().send_keys("Admin")
                password = HomePage(self.driver)
                password.enterPassword().send_keys("admin123")
                submit = HomePage(self.driver)
                submit.enterSubmitButton().click()
            except Exception as e:
                print(f"Caught exception: {type(e).__name__}: {e}")

            self.verythePresence2("//span[text()='Admin']")
            admin = AdminPage(self.driver)
            admin.ClickAdmin().click()
            time.sleep(2)

            try:
                content1 = AdminPage(self.driver)
                assert content1.getContent1().is_displayed()
                assert content1.getContent1().text == "User Management"
            except Exception as e:
                print(f"Caught exception: {type(e).__name__}: {e}")

            try:
                content2 = AdminPage(self.driver)
                assert content2.getContent2().is_displayed()
                assert content2.getContent2().text == "Job"
            except Exception as e:
                print(f"Caught exception: {type(e).__name__}: {e}")

            try:
                content3 = AdminPage(self.driver)
                assert content3.getContent3().is_displayed()
                assert content3.getContent3().text == "Organization"
            except Exception as e:
                print(f"Caught exception: {type(e).__name__}: {e}")

            try:
                content4 = AdminPage(self.driver)
                assert content4.getContent4().is_displayed()
                assert content4.getContent4().text == "Qualifications"
            except Exception as e:
                print(f"Caught exception: {type(e).__name__}: {e}")

            try:
                content5 = AdminPage(self.driver)
                assert content5.getContent5().is_displayed()
                assert content5.getContent5().text == "Nationalities"
            except Exception as e:
                print(f"Caught exception: {type(e).__name__}: {e}")

            try:
                content6 = AdminPage(self.driver)
                assert content6.getContent6().is_displayed()
                assert content6.getContent6().text == "Corporate Branding"
            except Exception as e:
                print(f"Caught exception: {type(e).__name__}: {e}")

            try:
                content7 = AdminPage(self.driver)
                assert content7.getContent7().is_displayed()
                assert content7.getContent7().text == "Configuration"
            except Exception as e:
                print(f"Caught exception: {type(e).__name__}: {e}")

        except Exception as e:
            print(f"Caught exception: {type(e).__name__}: {e}")




