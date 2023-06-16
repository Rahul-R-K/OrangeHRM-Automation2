from selenium.webdriver.common.by import By

class MenuPage:

    def __init__(self,driver):
        self.driver = driver

    Menu1 = (By.XPATH,"//span[text()='Admin']")
    Menu2 = (By.XPATH,"//span[text()='PIM']")
    Menu3 = (By.XPATH,"//span[text()='Leave']")
    Menu4 = (By.XPATH,"//span[text()='Time']")
    Menu5 = (By.XPATH, "//span[text()='Recruitment']")
    Menu6 = (By.XPATH, "//span[text()='My Info']")
    Menu7 = (By.XPATH, "//span[text()='Performance']")
    Menu8 = (By.XPATH, "//span[text()='Dashboard']")
    Menu9 = (By.XPATH, "//span[text()='Directory']")
    Menu10 = (By.XPATH, "//span[text()='Maintenance']")
    Menu11 = (By.XPATH, "//span[text()='Buzz']")




    def getMenu1(self):
        return self.driver.find_element(*MenuPage.Menu1)
    def getMenu2(self):
        return self.driver.find_element(*MenuPage.Menu2)
    def getMenu3(self):
        return self.driver.find_element(*MenuPage.Menu3)
    def getMenu4(self):
        return self.driver.find_element(*MenuPage.Menu4)
    def getMenu5(self):
        return self.driver.find_element(*MenuPage.Menu5)
    def getMenu6(self):
        return self.driver.find_element(*MenuPage.Menu6)
    def getMenu7(self):
        return self.driver.find_element(*MenuPage.Menu7)
    def getMenu8(self):
        return self.driver.find_element(*MenuPage.Menu8)
    def getMenu9(self):
        return self.driver.find_element(*MenuPage.Menu9)
    def getMenu10(self):
        return self.driver.find_element(*MenuPage.Menu10)
    def getMenu11(self):
        return self.driver.find_element(*MenuPage.Menu11)