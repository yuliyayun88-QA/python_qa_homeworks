from selenium import webdriver
from selenium.webdriver.common.by import By


def test_multiple_elements():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online/links/10")

# Найдите все ссылки на странице (тег <a>).
    links = driver.find_elements(By.CSS_SELECTOR, "div.links a")

# Проверьте, что количество ссылок равно 9.
    assert len(links) == 9, f"Ожидалось 9 ссылок, найдено: {len(links)}"

# Проверьте, что все ссылки отображаются на странице.
    for n in links:
        assert n.is_displayed(), f"Ссылка с текстом '{n.text}' не отображается"

# Проверьте, что текст первой ссылки содержит"1".
    assert links[0].text == "1", f"Текст первой ссылки: {links[0].text}"

    driver.quit()
