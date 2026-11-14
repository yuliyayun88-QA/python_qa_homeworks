import pytest
from selenium import webdriver

@pytest.mark.parametrize("browser_name", ["chrome", "edge", "yandex"])
def test_google_on_multiple_browsers(browser_name):
    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "edge":
        driver = webdriver.Edge()
    elif browser_name == "yandex":
        options = webdriver.ChromeOptions()
        options.binary_location = r"C:\Users\Ирина\AppData\Local\Yandex\YandexBrowser\Application\browser.exe"
        driver = webdriver.Chrome(options=options)
    else:
        raise ValueError("Неизвестный браузер")

    try:
        driver.get("https://www.google.com")
        assert "Google" in driver.title
    finally:
        driver.quit()