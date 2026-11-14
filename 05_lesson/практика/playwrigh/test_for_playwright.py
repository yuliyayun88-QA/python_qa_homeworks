from playwright.sync_api import Page, expect
import time


#Открыть страницу авторизации: https://ru.yougile.com/team/
def test_yougile_login(page: Page):
    page.goto("https://ru.yougile.com/team/")

# Ввести логин в поле «Email» sky-best-student@yandex.ru [autocomplete="email"]
    page.locator(
        "[autocomplete='email']").fill("sky-best-student@yandex.ru")

# Ввести пароль в поле «Пароль» Sky_Pro1 [autocomplete="current-password"]
    page.locator(
        "[autocomplete='current-password']").fill("Sky_Pro1")

# Нажать кнопку «Войти». .bg-action-default[role="button"]
    page.locator('.bg-action-default[role="button"]').click()
    time.sleep(5)
# Переход на страницу настроек аккаунта
    page.goto("https://ru.yougile.com/team/settings-account")
    time.sleep(5)

    user_name = page.locator("[placeholder='Отображаемое имя…']")

    expect(user_name).to_be_visible()
    expect(user_name).to_have_value("Sky_Pro")
