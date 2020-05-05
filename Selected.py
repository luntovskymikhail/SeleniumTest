from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:\Drivers\operadriver.exe")

#check radio button
driver.get("http://www.echoecho.com/htmlforms10.htm")

butterradio = driver.find_element_by_css_selector("input[value=Butter]")
if butterradio.is_selected() == True:
    print("butter radio is selected")
else:
    print("butter radio is not selected")

milkradio = driver.find_element_by_css_selector("input[value=Milk]")
if milkradio.is_selected() == True:
    print("milk radio is selected")
else:
    print("milk radio is not selected")

driver.quit()

#result
#butter radio is selected
#milk radio is not selected