import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        # webdriver.Chrome(ChromeDriverManager().install())
        # webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.url = "https://www.saucedemo.com/"
 
    def test_a_success_login(self):
        # steps
        driver = self.browser #buka web browser
        driver.get(self.url) # buka situs
        #time.sleep(3)
        driver.find_element(By.ID,"user-name").send_keys("standard_user") # isi email
        #time.sleep(1)
        driver.find_element(By.ID,"password").send_keys("secret_sauce") # isi password
        #time.sleep(1)
        driver.find_element(By.ID, "login-button").click()
        #time.sleep(1)
        # validasi
        response_data = driver.find_element(By.CLASS_NAME,"title").text
        self.assertIn('Products', response_data)

    def test_a_failed_login(self):
        # steps
        driver = self.browser #buka web browser
        driver.get(self.url) # buka situs
        #time.sleep(3)
        driver.find_element(By.ID,"user-name").send_keys("xxx_user") # isi email
        #time.sleep(1)
        driver.find_element(By.ID,"password").send_keys("xxx_sauce") # isi password
        #time.sleep(1)
        driver.find_element(By.ID, "login-button").click()
        # validasi
        response_data = driver.find_element(By.CSS_SELECTOR,"[data-test='error']").text
        self.assertIn('Epic sadface: Username and password do not match any user in this service', response_data)

    def test_a_failed_login_empty_username(self):
        # steps
        driver = self.browser #buka web browser
        driver.get(self.url) # buka situs
        #time.sleep(3)
        driver.find_element(By.ID,"user-name").send_keys("") # isi email
        #time.sleep(1)
        driver.find_element(By.ID,"password").send_keys("secret_sauce") # isi password
        #time.sleep(1)
        driver.find_element(By.ID, "login-button").click()
        # validasi
        response_data = driver.find_element(By.CSS_SELECTOR,"[data-test='error']").text
        self.assertIn('Epic sadface: Username is required', response_data)

    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()
