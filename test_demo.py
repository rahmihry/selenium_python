from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from time import sleep

# Set options for not prompting DevTools information
options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

print("testing started")
driver = webdriver.Chrome(options=options)

driver.get("https://www.saucedemo.com/")
sleep(3)

# Find element using element's id attribute
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
sleep(5)

text = driver.find_element(By.CLASS_NAME, "title").text

# Check if login was successful 
assert "products" in text.lower()

print("TEST PASSED : LOGIN SUCCESSFUL", "\n")

print("testing add to cart")
add_to_cart_btns = driver.find_elements(By.CLASS_NAME, "btn_inventory")

# Click three buttons to make the cart_value 3
for btns in add_to_cart_btns[:3]:
    btns.click()

    cart_value = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
assert "3" in cart_value.text
print("TEST PASSED : ADD TO CART", "\n")

print("testing remove from cart")
remove_btns = driver.find_elements(By.CLASS_NAME, "btn_inventory")
for btns in remove_btns[:2]:
    btns.click()
assert "1" in cart_value.text
print("TEST PASSED : REMOVE FROM CART", "\n")

# Close the driver
driver.quit()
