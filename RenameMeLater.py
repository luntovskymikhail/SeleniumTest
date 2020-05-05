from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:\Drivers\operadriver.exe")

driver.maximize_window()
driver.get("https://yandex.ru/")

driver.find_element_by_id('//*[@id="taw0"]/div[5]/a').click()

#/html/body/div[2]/div[2]/div[3]/div/div[2]/div/edvrt/div/div/div[1]/div/div/a[5]