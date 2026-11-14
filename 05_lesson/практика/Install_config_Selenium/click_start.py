from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://gitflic.ru")

sleep(2)

# Кликаем по кнопке
click_button = driver.find_element(By.CLASS_NAME, "button-start")
click_button.click()
sleep(2)

# Закрываем браузер
driver.quit()
