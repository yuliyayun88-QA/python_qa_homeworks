from selenium import webdriver
from selenium.webdriver.common.by import By

def test_element_state():
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/radio-button")

    # Найдите радио-кнопку "Yes"
    radio_but = driver.find_element(By.ID, "yesRadio")
    # 1. и проверьте Что она отображается
    assert radio_but.is_displayed(), "Кнопка не видна"
    # 2. Что она доступна для клика
    assert radio_but.is_enabled(), "Кнопка не активна"

    driver.quit()