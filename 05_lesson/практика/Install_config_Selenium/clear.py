from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://gitflic.ru")
driver.maximize_window()  # Разворачиваем окно на весь экран

# Закрываем баннер с куки
driver.find_element(By.CLASS_NAME, "cookiesBtn").click()
sleep(2)

# Кликаем по кнопке "Начать работу"
click_button = driver.find_element(By.CLASS_NAME, "button-start")
click_button.click()
sleep(2)

# Вводим почту
input_login = driver.find_element(By.ID, "email")
input_login.send_keys("in6vq@airsworld.net")

# Вводим пароль
input_password = driver.find_element(By.ID, "passwordBasic")
input_password.send_keys("12345Qwerty")
sleep(3)

# Очищаем поле логина и пароля
# clear() работает только с полями ввода (<input>, <textarea>)
input_login.clear()
input_password.clear()

# Нажимаем кнопку входа
submit_button = driver.find_element(By.CLASS_NAME, "btn-success")
submit_button.click()
sleep(5)

driver.quit()