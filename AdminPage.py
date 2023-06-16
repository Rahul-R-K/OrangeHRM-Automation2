from selenium.webdriver.common.by import By

class AdminPage:

    def __init__(self,driver):
        self.driver = driver

    Admin = (By.XPATH,"//span[text()='Admin']")
    Content1 = (By.XPATH,"(//header//li[1]//span[1])[2]")
    Content2 = (By.XPATH,"(//header//li[2]//span[1])")
    Content3 = (By.XPATH,"(//header//li[3]//span[1])")
    Content4 = (By.XPATH,"(//header//li[4]//span[1])")
    Content5 = (By.XPATH, "(//header//li[5]//a[1])")
    Content6 = (By.XPATH, "(//header//li[6]//a[1])")
    Content7 = (By.XPATH, "(//header//li[7]//span[1])")



    def ClickAdmin(self):
        return self.driver.find_element(*AdminPage.Admin)
    def getContent1(self):
        return self.driver.find_element(*AdminPage.Content1)
    def getContent2(self):
        return self.driver.find_element(*AdminPage.Content2)
    def getContent3(self):
        return self.driver.find_element(*AdminPage.Content3)
    def getContent4(self):
        return self.driver.find_element(*AdminPage.Content4)
    def getContent5(self):
        return self.driver.find_element(*AdminPage.Content5)
    def getContent6(self):
        return self.driver.find_element(*AdminPage.Content6)
    def getContent7(self):
        return self.driver.find_element(*AdminPage.Content7)
