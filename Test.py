from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="C:\Drivers\operadriver.exe")
def wait():
    time.sleep(13)

#open main page
driver.get("https://www.spbrealty.ru/")
wait()

#goes to about company
driver.find_element_by_xpath('//*[@id="emerge-header"]/div[3]/div/div/div[1]/ul/li[4]/a').click()
wait()

driver.back()
wait()

driver.forward()
wait()

driver.quit()