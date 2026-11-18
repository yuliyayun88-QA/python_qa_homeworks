from time import sleep
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://gitflic.ru/")

#cookies = driver.get_cookies()
#for cookie in cookies:
    #print(f"{cookie['name']}: {cookie['value']}")

driver.add_cookie({
    "name": "SESSION",
    "value": "ZTlmOGNiNTItZjU1My00MjkzLTliYWUtZTU0OWIyNzI1NjJk",
    "domain": "gitflic.ru"
})
driver.add_cookie({
    "name": "cookiesAccepted",
    "value": "true",
    "domain": "gitflic.ru"
})

driver.refresh()
driver.get("https://gitflic.ru/user/airsworld")

sleep(5)

driver.delete_all_cookies()
driver.refresh()
sleep(5)

driver.quit()
