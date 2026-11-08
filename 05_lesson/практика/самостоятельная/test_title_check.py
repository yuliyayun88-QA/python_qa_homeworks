from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_page_title():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online/")
    sleep(5)

# Найдите элемент h1 и проверьте его текст
    element_h1 = driver.find_element(By.TAG_NAME, "h1")
    assert "httpbin" in element_h1.text.lower()

    driver.quit()
