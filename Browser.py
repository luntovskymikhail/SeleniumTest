from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
driver.get("https://yandex.ru/")
name = "Яндекс"
if driver.title == name:
    print("Pass - Заголовок")
else:
    print("Fail - Заголовок")
driver.close()