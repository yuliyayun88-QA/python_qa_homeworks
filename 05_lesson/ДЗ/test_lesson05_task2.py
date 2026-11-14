from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form_submission():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online/forms/post")

# Запомним URL страницы до отправки формы
    url_before = driver.current_url

# Найдите поле ввода с названием custname.
    element = driver.find_element(By.NAME, "custname")

# Введите в него ваше имя.
    element.send_keys("Юлия")

# Найдите кнопку Submit и нажмите на нее.
    driver.find_element(By.XPATH, "//button[text()='Submit']").click()

# Проверьте, что после нажатия URL изменился.
    sleep(3)
    url_after = driver.current_url

    assert driver.title == "Форма отправлена — httpbin", \
        f"Заголовок не изменился: {driver.title}"

    assert url_after != url_before, f"URL неизменился: {url_after}"

    driver.quit()
