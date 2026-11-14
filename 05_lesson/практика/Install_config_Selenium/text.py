from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://gitflic.ru")
driver.maximize_window()

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

# Нажимаем кнопку входа
submit_button = driver.find_element(By.CLASS_NAME, "btn-success")
submit_button.click()
sleep(5)

# Находим элемент с именем пользователя и выводим его текст
user_name = driver.find_element(
    By.CLASS_NAME, "profile-page__profile-name")
print(user_name.text)

# text возвращает только видимый текст. Если элемент скрыт через CSS, text вернет пустую строку.
# text не возвращает текст из атрибутов (например, placeholder или value). Для этого используйте метод
# get_attribute().
driver.quit()