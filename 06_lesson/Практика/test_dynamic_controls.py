from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_dynamic_controls():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    driver.get("https://the-internet.herokuapp.com/dynamic_controls")

    # Нажмите кнопку Remove
    remove_button = driver.find_element(
        By.CSS_SELECTOR, 'button[onclick="swapCheckbox()"]')
    remove_button.click()

    # Дождитесь появления текста It's gone!
    text = wait.until(EC.text_to_be_present_in_element(
        (By.CSS_SELECTOR, "p#message"), "It's gone!"))
    message = driver.find_element(By.CSS_SELECTOR, "p#message")
    assert message.text == "It's gone!", "Сообщение 'It's gone!' не появилось"

    # Нажмите кнопку Enable.
    enable_btn = driver.find_element(By.XPATH, "//button[text()='Enable']")
    enable_btn.click()

    # Дождитесь, когда поле ввода станет активным.
    input_field = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//input[@type='text']"))
    )
    assert input_field.is_enabled(), "Поле ввода не стало активным"

    # Проверьте, что поле действительно стало активным.
    input_field.send_keys("Hello World")
    assert input_field.get_attribute("value") == "Hello World", "Текст не ввелся в поле"

    driver.quit()