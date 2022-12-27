import re
from playwright.sync_api import Page, expect

def test_login(page: Page):
    page.goto("http://users.bugred.ru/user/login/index.html/")
    page.locator("input[name=\"name\"]").click()
    page.locator("input[name=\"name\"]").fill("Sam")
    page.locator("input[name=\"email\"]").click()
    page.locator("input[name=\"email\"]").fill("san@gmail.com")
    page.get_by_role("rowgroup").filter(has_text="Имя Email Пароль Зарегистрироваться").locator("input[name=\"password\"]").click()
    page.get_by_role("rowgroup").filter(has_text="Имя Email Пароль Зарегистрироваться").locator("input[name=\"password\"]").fill("qwerty")
    page.get_by_role("button", name="Зарегистрироваться").click()


#def test_users_on_the_site(page: Page):

    #page.goto('http://users.bugred.ru/user/login/index/')
    #page.fill('input#type-email', 'chack@gmail.com')
    #page.fill('input#type-password', 'qwerty')
    #page.click('button[type=submit]')