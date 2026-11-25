from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_form():
    driver = webdriver.Edge()
    wait = WebDriverWait(driver, 15)

    # Откройте страницу
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    driver.maximize_window()

    # Заполните форму
    form_data = {
        (By.NAME, "first-name"): "Иван",
        (By.NAME, "last-name"): "Петров",
        (By.CSS_SELECTOR, "input[name='address']"): "Ленина, 55-3",
        (By.CSS_SELECTOR, "input[name='city']"): "Москва",
        (By.CSS_SELECTOR, "input[name='country']"): "Россия",
        (By.CSS_SELECTOR, "input[name='e-mail']"): "test@skypro.com",
        (By.CSS_SELECTOR, "input[name='phone']"): "+7985899998787",
        (By.NAME, "job-position"): "QA",
        (By.CSS_SELECTOR, "input[name='company']"): "SkyPro",
    }

    for locator, value in form_data.items():
        wait.until(EC.visibility_of_element_located(locator)).send_keys(value)

    # Нажмите кнопку Submit
    submit = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[normalize-space()='Submit']")))
    driver.execute_script("arguments[0].click();", submit)

    print("URL после Submit:", driver.current_url)
    driver.save_screenshot("after_submit.png")

    # Проверьте (assert), что поле Zip code подсвечено красным
    wait.until(EC.text_to_be_present_in_element_attribute(
        (By.ID, "zip-code"), "class", "alert-danger"))

    zip_code = driver.find_element(By.ID, "zip-code")
    assert "alert-danger" in zip_code.get_attribute("class"), \
        "Поле zip code не подсвечено красным"

    # Проверьте(assert), что остальные поля подсвечены зеленым
    green_fields = [
        (By.ID, "first-name"),
        (By.ID, "last-name"),
        (By.ID, "address"),
        (By.ID, "city"),
        (By.ID, "country"),
        (By.ID, "e-mail"),
        (By.ID, "phone"),
        (By.ID, "job-position"),
        (By.ID, "company"),
    ]

    for locator in green_fields:
        element = wait.until(EC.visibility_of_element_located(locator))
        classes = element.get_attribute("class")
        assert "alert-succes" in classes, \
            f"Поле {locator[1]} не подсвечено зелёным, классы: {classes}"

    print("Тест пройден")

    driver.quit()
