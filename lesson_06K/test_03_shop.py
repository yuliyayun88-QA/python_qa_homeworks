from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_shop():
    # 1. Открываем сайт магазина в Firefox
    driver = webdriver.Firefox()
    wait = WebDriverWait(driver, 15)

    driver.get("https://www.saucedemo.com/")

    # 2. Авторизуемся как пользователь standard_user
    wait.until(EC.visibility_of_element_located
               ((By.ID, "user-name"))).send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # 3. Добавляем в корзину товары
    wait.until(EC.element_to_be_clickable
               ((By.ID, "add-to-cart-sauce-labs-backpack"))).click()
    # Sauce Labs Bolt T-Shirt
    wait.until(EC.element_to_be_clickable
               ((By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"))).click()
    # Sauce Labs Onesie
    wait.until(EC.element_to_be_clickable
               ((By.ID, "add-to-cart-sauce-labs-onesie"))).click()

    shopping = wait.until(EC.visibility_of_element_located
                          ((By.CLASS_NAME, "shopping_cart_link")))
    # Проверяем, что в корзине есть товар
    label_text = shopping.text  # 3
    assert label_text == "3", (
        "Ярлыка с количеством на корзине не появилось или он не совпадает")

    # 4. Переходим в корзину
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    # 5. Нажимаем Checkout
    wait.until(EC.element_to_be_clickable((By.ID, "checkout"))).click()

    # 6. Заполняем форму своими данными
    wait.until(EC.visibility_of_element_located
               ((By.ID, "first-name"))).send_keys("Ulia")

    driver.find_element(By.ID, "last-name").send_keys("Un")

    driver.find_element(By.ID, "postal-code").send_keys("123456")

    # 7. Нажимаем кнопку Continue
    wait.until(EC.element_to_be_clickable((By.ID, "continue"))).click()

    # 8. Читаем со страницы итоговую стоимость (Total)
    wait.until(EC.url_contains("/checkout-step-two.html"))

    total_price = wait.until(EC.visibility_of_element_located
                             ((By.CLASS_NAME, "summary_total_label"))).text

    # 10. Проверяем, что итоговая сумма равна \$58.29
    assert total_price == "Total: $58.29", (
        f"Ошибка: ожидалось 'Total: $58.29', но получено '{total_price}'")

    driver.quit()
