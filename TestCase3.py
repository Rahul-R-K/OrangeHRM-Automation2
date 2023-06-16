import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from BaseClass import BaseClass
from LoginPage import HomePage
#from AdminPage import AdminPage
from MenuPage import MenuPage

class Testcase3(BaseClass):

    def test_TC_PIM_03(self):
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

            try:
                menuPage = MenuPage(self.driver)
                menu_items = [menuPage.getMenu1, menuPage.getMenu2, menuPage.getMenu3, menuPage.getMenu4,
                              menuPage.getMenu5, menuPage.getMenu6, menuPage.getMenu7, menuPage.getMenu8,
                              menuPage.getMenu9, menuPage.getMenu10, menuPage.getMenu11]

                for get_menu in menu_items:
                    try:
                        assert get_menu().is_displayed()
                    except Exception as e:
                        print(f"Caught exception: {type(e).__name__}: {e}")

            except Exception as e:
                print(f"Caught exception: {type(e).__name__}: {e}")

        except Exception as e:
            print(f"Caught exception: {type(e).__name__}: {e}")

