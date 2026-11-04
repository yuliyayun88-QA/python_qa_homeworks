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

# Находим поле почты по ID и вводим логин
input_login = driver.find_element(By.ID, "email")
input_login.send_keys("in6vq@airsworld.net")

# Находим поле пароля по ID и вводим пароль
input_password = driver.find_element(By.ID, "passwordBasic")
input_password.send_keys("12345Qwerty")

# Нажимаем кнопку входа
submit_button = driver.find_element(By.CLASS_NAME, "btn-success")
submit_button.click()
sleep(5)

driver.quit()
