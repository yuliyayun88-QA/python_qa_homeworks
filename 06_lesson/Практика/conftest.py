import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://gitflic.ru/")
    driver.add_cookie({
        "name": "SESSION",
        "value": "NzY1MTEzNDgtNzhhYS00ZGU0LWFjOWUtYTg3NTIyN2IzMzA0",
        "domain": "gitflic.ru"
    })
    driver.add_cookie({
        "name": "cookiesAccepted",
        "value": "true",
        "domain": "gitflic.ru"
    })

    driver.refresh()
    yield driver
    driver.quit()
