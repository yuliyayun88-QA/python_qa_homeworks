from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_calc():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 46)

    # Откройте страницу
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    driver.maximize_window()

    # В поле ввода по локатору delay введите значение 45
    delay_field = driver.find_element(By.ID, "delay")
    delay_field.clear()
    delay_field.send_keys("45")

    # Нажмите на кнопки: 7 + 8 =
    for button in ["7", "+", "8", "="]:
        driver.find_element(By.XPATH, f"//span[text()='{button}']").click()

    # Проверьте, что в окне отобразится результат 15 через 45 секунд
    screen = driver.find_element(By.CSS_SELECTOR, ".screen")
    wait.until(EC.text_to_be_present_in_element
               ((By.CSS_SELECTOR, ".screen"), "15"))
    assert screen.text == "15", f"Ожидали 15, а увидели: {screen.text}"

    print("Тест пройден")

    driver.quit()
