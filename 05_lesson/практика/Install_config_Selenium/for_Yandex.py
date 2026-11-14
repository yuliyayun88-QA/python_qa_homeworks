import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.binary_location = r"C:\Users\Ирина\AppData\Local\Yandex\YandexBrowser\Application\browser.exe"

service = Service(ChromeDriverManager().install())
yandex_driver = webdriver.Chrome(service=service, options=options)

# Открываем страницу
print("Открытие страницы Google...")
yandex_driver.get("https://www.google.com")

time.sleep(5)

print("Текущий заголовок страницы:", yandex_driver.title)

# Закрываем браузер
print("Закрытие браузера...")
yandex_driver.quit()
