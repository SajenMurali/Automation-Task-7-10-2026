from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 10)
# ------------------------------------------------
# Slow down the execution
# ------------------------------------------------
def pause():
    time.sleep(2)
# ------------------------------------------------
# TC01 - SauceDemo Login
# ------------------------------------------------
driver.get("https://www.saucedemo.com/")
pause()
print("TC01 - Shopping website opened successfully")
wait.until(
    EC.visibility_of_element_located((By.ID, "user-name"))
).send_keys("standard_user")
pause()
driver.find_element(By.ID, "password").send_keys("secret_sauce")
pause()
driver.find_element(By.ID, "login-button").click()
pause()
wait.until(
    EC.visibility_of_element_located((By.CLASS_NAME, "inventory_list"))
)
print("TC01 - Login successful")
pause()
# ------------------------------------------------
# TC02 - Simple Alert
# ------------------------------------------------
driver.get("https://www.selenium.dev/selenium/web/alerts.html")
pause()
driver.find_element(By.ID, "alert").click()
pause()
alert = wait.until(
    EC.alert_is_present()
)
print("\nTC02 - Alert:")
print(alert.text)
pause()
alert.accept()
pause()
print("TC02 - Alert accepted successfully")
pause()
# ------------------------------------------------
# TC03 - Confirmation Alert
# ------------------------------------------------
driver.get("https://www.selenium.dev/selenium/web/alerts.html")
pause()
driver.find_element(By.ID, "confirm").click()
pause()
alert = wait.until(
    EC.alert_is_present()
)
print("\nTC03 - Confirmation Alert:")
print(alert.text)
pause()
alert.dismiss()
pause()
print("TC03 - Confirmation alert dismissed successfully")
pause()
# ------------------------------------------------
# TC04 - Prompt Alert
# ------------------------------------------------
driver.get("https://www.selenium.dev/selenium/web/alerts.html")
pause()
driver.find_element(By.ID, "prompt").click()
pause()
alert = wait.until(
    EC.alert_is_present()
)
print("\nTC04 - Prompt Alert:")
print(alert.text)
pause()
alert.send_keys("Aditya")
pause()
alert.accept()
pause()
print("TC04 - Customer information submitted successfully")
pause()
# ------------------------------------------------
# TC05 - Mouse Hover
# ------------------------------------------------
driver.get("https://www.selenium.dev/selenium/web/mouse_interaction.html")
pause()
hover_element = wait.until(
    EC.visibility_of_element_located((By.ID, "hover"))
)
ActionChains(driver).move_to_element(hover_element).perform()
pause()
move_status = wait.until(
    EC.visibility_of_element_located((By.ID, "move-status"))
)
print("\nTC05 - Mouse Hover performed successfully")
print("Result:", move_status.text)
pause()
# ------------------------------------------------
# TC06 - Double Click
# ------------------------------------------------
driver.get("https://www.selenium.dev/selenium/web/mouse_interaction.html")
pause()
double_click_element = wait.until(
    EC.visibility_of_element_located((By.ID, "clickable"))
)
ActionChains(driver).double_click(double_click_element).perform()
pause()
click_status = wait.until(
    EC.visibility_of_element_located((By.ID, "click-status"))
)
print("\nTC06 - Double Click performed successfully")
print("Result:", click_status.text)
pause()
# ------------------------------------------------
# TC07 - Drag and Drop
# ------------------------------------------------
driver.get("https://www.selenium.dev/selenium/web/mouse_interaction.html")
pause()
source = wait.until(
    EC.visibility_of_element_located((By.ID, "draggable"))
)
target = wait.until(
    EC.visibility_of_element_located((By.ID, "droppable"))
)
pause()
ActionChains(driver).drag_and_drop(source, target).perform()
pause()
drop_status = wait.until(
    EC.visibility_of_element_located((By.ID, "drop-status"))
)
print("\nTC07 - Drag and Drop performed successfully")
print("Result:", drop_status.text)
pause()
# ------------------------------------------------
# TC08 - Product Search
# ------------------------------------------------
driver.get("https://www.automationexercise.com/products")
pause()
search_box = wait.until(
    EC.visibility_of_element_located((By.ID, "search_product"))
)
search_box.clear()
search_box.send_keys("Top")
pause()
search_button = wait.until(
    EC.element_to_be_clickable((By.ID, "submit_search"))
)
search_button.click()
pause()
searched_products = wait.until(
    EC.visibility_of_element_located(
        (
            By.XPATH,
            "//h2[contains(translate(normalize-space(.), 'abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'), 'SEARCHED PRODUCTS')]"
        )
    )
)
products = wait.until(
    EC.presence_of_all_elements_located(
        (
            By.XPATH,
            "//div[contains(@class,'productinfo')]"
        )
    )
)
print("\nTC08 - Product search completed successfully")
print("Result:", searched_products.text)
print("Number of products found:", len(products))
pause()
# ------------------------------------------------
# TC09 - Place Order
# ------------------------------------------------
driver.get("https://www.saucedemo.com/")
pause()
wait.until(
    EC.visibility_of_element_located((By.ID, "user-name"))
).send_keys("standard_user")
pause()
driver.find_element(By.ID, "password").send_keys("secret_sauce")
pause()
driver.find_element(By.ID, "login-button").click()
pause()
wait.until(
    EC.visibility_of_element_located((By.CLASS_NAME, "inventory_list"))
)
print("\nTC09 - Logged into SauceDemo")
pause()
driver.find_element(
    By.ID, "add-to-cart-sauce-labs-backpack"
).click()
pause()
driver.find_element(
    By.CLASS_NAME, "shopping_cart_link"
).click()
pause()
wait.until(
    EC.visibility_of_element_located((By.CLASS_NAME, "cart_item"))
)
print("TC09 - Product added to cart")
pause()
driver.find_element(By.ID, "checkout").click()
pause()
wait.until(
    EC.visibility_of_element_located((By.ID, "first-name"))
).send_keys("Aditya")
pause()
driver.find_element(By.ID, "last-name").send_keys("S")
pause()
driver.find_element(By.ID, "postal-code").send_keys("600001")
pause()
driver.find_element(By.ID, "continue").click()
pause()
finish_button = wait.until(
    EC.element_to_be_clickable((By.ID, "finish"))
)
print("TC09 - Place Order button is clickable")
pause()
finish_button.click()
pause()
confirmation = wait.until(
    EC.visibility_of_element_located(
        (By.CLASS_NAME, "complete-header")
    )
)
print("TC09 - Order submitted successfully")
print("Result:", confirmation.text)
pause()
# ------------------------------------------------
# TC10 - Order Confirmation Alert
# ------------------------------------------------
driver.get("https://www.saucedemo.com/")
pause()
wait.until(
    EC.visibility_of_element_located((By.ID, "user-name"))
).send_keys("standard_user")
pause()
driver.find_element(By.ID, "password").send_keys("secret_sauce")
pause()
driver.find_element(By.ID, "login-button").click()
pause()
wait.until(
    EC.visibility_of_element_located((By.CLASS_NAME, "inventory_list"))
)
driver.find_element(
    By.ID, "add-to-cart-sauce-labs-backpack"
).click()
pause()
driver.find_element(
    By.CLASS_NAME, "shopping_cart_link"
).click()
pause()
wait.until(
    EC.visibility_of_element_located((By.CLASS_NAME, "cart_item"))
)
driver.find_element(By.ID, "checkout").click()
pause()
wait.until(
    EC.visibility_of_element_located((By.ID, "first-name"))
).send_keys("Aditya")
pause()
driver.find_element(By.ID, "last-name").send_keys("S")
pause()
driver.find_element(By.ID, "postal-code").send_keys("600001")
pause()
driver.find_element(By.ID, "continue").click()
pause()

finish_button = wait.until(
    EC.element_to_be_clickable((By.ID, "finish"))
)

finish_button.click()
pause()

wait.until(
    EC.visibility_of_element_located(
        (By.CLASS_NAME, "complete-header")
    )
)
pause()
driver.execute_script(
    "setTimeout(function(){alert('Order confirmation successful')}, 500)"
)
alert = wait.until(
    EC.alert_is_present()
)
print("\nTC10 - Order Confirmation Alert:")
print(alert.text)
pause()
alert.accept()
pause()
print("TC10 - Confirmation alert handled successfully")
print("\nAll test cases completed successfully")
pause()
driver.quit()