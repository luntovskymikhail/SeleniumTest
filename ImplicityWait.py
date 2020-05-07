from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="C:\Drivers\operadriver.exe")

#runs lk page
driver.maximize_window()
driver.get("https://lk.spbrealty.ru/auth")
driver.implicitly_wait(1)

#login into lk
driver.find_element_by_name("phone").send_keys("9523813251")
driver.find_element_by_name("password").send_keys("94!h87!D")
driver.find_element_by_xpath('//*[@id="__layout"]/div/div[2]/div/div/div/div[1]/form/div[3]/div[1]/button').click()

#shows result of code above
time.sleep(17)
driver.quit()