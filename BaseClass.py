import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import pyautogui

@pytest.mark.usefixtures("setup")
class BaseClass:
    def verifythePresence(self, text):
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.NAME, text)))
    def verythePresence2(self,text):
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, text)))
    def verifyaddpresence(self,text):
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, text)))
    def verifyeditpresence(self,text):
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, text)))
    def verifyNmaePresence(self,text):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, text)))
    def verifydeletePresence(self,text):
        WebDriverWait(self.driver, 30).until(
        EC.presence_of_element_located((By.XPATH, text)))
    def HandelExeption(self):
        self.driver.close()
        s_obj = Service(executable_path="D:\Rahul Files\C Files\PycharmProjects\Demo\chromedriver.exe")
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(service=s_obj, options=options)
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        return driver.maximize_window()

