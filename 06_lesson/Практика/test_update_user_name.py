from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_update_user_name(driver):
    wait = WebDriverWait(driver, 15)

    #Перейти на страницу профиля
    driver.get("https://gitflic.ru/user/airsworld")

    driver.save_screenshot("Screenshots/page.png")

    # Нажать кнопку редактирования профиля
    edit_button = wait.until(EC.presence_of_element_located(
        (By.CLASS_NAME, "user-profile__edit")
    ))
    edit_button.click()

    # Изменить Ф и И в форме
    username_input = wait.until(EC.presence_of_element_located(
        (By.ID, "name")
    ))
    username_input.clear()
    username_input.send_keys("alis")

    surname_input = driver.find_element(By.ID, "surname")
    surname_input.clear()
    surname_input.send_keys("son")

    # Сохранить изменения
    save_button = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, ".gf-button.--success")
    ))
    save_button.click()

    # Вернуться на страницу профиля
    driver.get("https://gitflic.ru/user/airsworld")

    driver.save_screenshot("Screenshots/page_after.png")

    # Ожидаемый результат: Ф и И успешно изменены и отображаются на странице профиля
    user_name = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, "h6.mb-0")
    ))
    user_name.screenshot("Screenshots/name.png")

    assert user_name.text == "alis son"
