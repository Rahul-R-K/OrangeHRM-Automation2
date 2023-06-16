import time
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
import pyautogui



@pytest.fixture(scope="class")
def setup(request):
    s_obj = Service(executable_path="D:\Rahul Files\C Files\PycharmProjects\Demo\chromedriver.exe")
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(service=s_obj, options=options)
    try:
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        driver.maximize_window()
    except:
        print("WebPage is Not Working")
    request.cls.driver = driver
    yield
    time.sleep(10)
    driver.close()
