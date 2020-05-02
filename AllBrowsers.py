from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driveredge = webdriver.Edge(executable_path="C:\Drivers\msedgedriver.exe")
driverchrome = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
driverfirefox = webdriver.Firefox(executable_path="C:\Drivers\geckodriver.exe")
driverie = webdriver.Ie(executable_path="C:\Drivers\IEDriverServer.exe")
driveropera = webdriver.Opera(executable_path="C:\Drivers\operadriver.exe")

#edge
driveredge.get("https://yandex.ru/")
name = "Яндекс"
if driveredge.title == name:
    print("Pass - Заголовок Edge")
else:
    print("Fail - Заголовок Edge")
driveredge.close()

#chrome
driverchrome.get("https://yandex.ru/")
name = "Яндекс"
if driverchrome.title == name:
    print("Pass - Заголовок Chrome")
else:
    print("Fail - Заголовок Chrome")
driverchrome.close()

#firefox
driverfirefox.get("https://yandex.ru/")
name = "Яндекс"
if driverfirefox.title == name:
    print("Pass - Заголовок Firefox")
else:
    print("Fail - Заголовок Firefox")
driverfirefox.close()

#internet explorer
driverie.get("https://yandex.ru/")
name = "Яндекс"
if driverie.title == name:
    print("Pass - Заголовок IE")
else:
    print("Fail - Заголовок IE")
driverie.close()

#opera
driveropera.get("https://yandex.ru/")
name = "Яндекс"
if driveropera.title == name:
    print("Pass - Заголовок Opera")
else:
    print("Fail - Заголовок Opera")
driveropera.close()