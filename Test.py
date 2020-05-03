from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="C:\Drivers\operadriver.exe")
def wait():
    time.sleep(7)

#open main page
driver.get("https://www.spbrealty.ru/")
wait()

element = driver.find_element_by_name("NewObjectMailing[email]")
if element.is_displayed() == True:
    print("Element is displayed")
else:
    print("Element is not displayed")

if element.is_enabled() == True:
    print("Element is enabled")
else:
    print("Element is not enabled")

element.send_keys("test@test.ru")