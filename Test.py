from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driverchrome = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")

driverchrome.get("https://vk.com/")

driverchrome.find_element_by_xpath('//*[@id="index_login_button"]').click()

time.sleep(5)

driverchrome.quit()