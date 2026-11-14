import time
from selenium import webdriver

print("Запуск браузера...")
driver = webdriver.Chrome()  # Создаем драйвер-Selenium Manager все сделает автоматически

# Открываем страницу
print("Открытие страницы Google...")
driver.get("https://www.google.com")

time.sleep(5)

# Выводим заголовок страницы
print("Текущий заголовок страницы:", driver.title)

# Выводим текущий URL
print("URL:", driver.current_url)

# Обновляем страницу
driver.refresh()

print("Закрытие браузера...")
driver.quit()

print("Скрипт выполнен успешно!")
