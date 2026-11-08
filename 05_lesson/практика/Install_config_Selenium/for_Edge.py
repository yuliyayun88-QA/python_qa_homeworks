import time
from selenium import webdriver

# Откроем Edge с помощью Selenium Manager
print("Запуск браузера...")
edge_driver = webdriver.Edge()

# Открываем страницу
print("Открытие страницы Google...")
edge_driver.get("https://www.google.com")

time.sleep(5)

print("Текущий заголовок страницы:", edge_driver.title)

# Выводим текущий URL
print("URL:", edge_driver.current_url)

# Закрываем браузер
print("Закрытие браузера...")
edge_driver.quit()
