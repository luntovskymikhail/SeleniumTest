from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driverc = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
driverf = webdriver.Firefox(executable_path="C:\Drivers\geckodriver.exe")
driverie = webdriver.Ie(executable_path="C:\Drivers\IEDriverServer.exe")

#chrome
driverc.get("https://yandex.ru/")
name = "Яндекс"
if driverc.title == name:
    print("Pass - Заголовок Chrome")
else:
    print("Fail - Заголовок Chrome")
driverc.close()

#firefox
driverf.get("https://yandex.ru/")
name = "Яндекс"
if driverf.title == name:
    print("Pass - Заголовок Firefox")
else:
    print("Fail - Заголовок Firefox")
driverf.close()

#internet explorer
driverie.get("https://yandex.ru/")
name = "Яндекс"
if driverie.title == name:
    print("Pass - Заголовок IE")
else:
    print("Fail - Заголовок IE")
driverie.close()