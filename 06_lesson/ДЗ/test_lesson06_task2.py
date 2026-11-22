from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_session_storage_auth():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 20)

    # Откройте страницу https://gitflic.ru/.
    driver.get("https://gitflic.ru/")

    # Установите cookie пользователя 1.
    driver.add_cookie({
        "name": "SESSION",
        "value": "OGUxZjM3OGQtYjYwMy00MDdjLTkyNjktM2ZmMjllYmIwZWU2",
        "domain": "gitflic.ru"
    })
    driver.add_cookie({
        "name": "cookiesAccepted",
        "value": "true",
        "domain": "gitflic.ru"
    })

    # Обновите страницу.
    driver.refresh()

    # Перейдите на страницу пользователя 1.
    driver.get("https://gitflic.ru/user/ulia")

    # Сохраните текущий URL.
    url_1 = driver.current_url
    assert "/user/ulia" in url_1, f"Текущий URL: {url_1}"
    print(f"URL первого пользователя: {url_1}")

    # Разлогиньтесь (очистите куки).
    driver.delete_all_cookies()
    driver.refresh()

    # Установите cookie пользователя 2.
    driver.add_cookie({
        "name": "SESSION",
        "value": "MzMzNWU2MWMtNjI5ZS00MmQxLTlkYjYtZWVmYmQxZWE4Mzkx",
        "domain": "gitflic.ru"
    })
    driver.add_cookie({
        "name": "cookiesAccepted",
        "value": "true",
        "domain": "gitflic.ru"
    })

    # Обновите страницу.
    driver.refresh()

    # Перейдите на страницу пользователя 2.
    driver.get("https://gitflic.ru/user/ylia")

    # Сохраните текущий URL.
    url_2 = driver.current_url
    assert "/user/ylia" in url_2, f"Текущий URL: {url_2}"
    print(f"URL второго пользователя: {url_2}")

    # Проверьте, что URL для пользователя 1 и пользователя 2 различаются.
    assert url_1 != url_2, "URL пользователей одинаковы"

    driver.quit()
