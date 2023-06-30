import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestAddtoCart(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        # webdriver.Chrome(ChromeDriverManager().install())
        # webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.url = "https://www.saucedemo.com/"
 
    def test_add_to_cart(self):
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

        driver.find_element(By.CSS_SELECTOR, "[data-test='add-to-cart-sauce-labs-bolt-t-shirt']").click()
        cart = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
        self.assertEqual(cart, "1")
        driver.find_element(By.CLASS_NAME, "shopping_cart_badge").click()
        url = driver.current_url
        self.assertIn('/cart.html', url)
        inventory = driver.find_element(By.CLASS_NAME, "inventory_item_name")

    
    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()