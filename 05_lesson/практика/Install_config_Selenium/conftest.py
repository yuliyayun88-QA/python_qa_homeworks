import pytest
from selenium import webdriver


# помещаем логику выбора браузера
def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        default="chrome",
        help="Выберите браузер: chrome или edge"
    )

@pytest.fixture(scope="session")
def driver(request):
    browser = request.config.getoption("--browser")

    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "edge":
        driver = webdriver.Edge()
    elif browser == "yandex":
        driver = webdriver.Yandex()
    else:
        raise pytest.UsageError(f"Неподдерживаемый браузер: {browser}")

    yield driver
    driver.quit()
