import re
from playwright.sync_api import Page, expect


def test_playwright(page: Page):     
    page.goto("https://ya.ru/?nr=1")
    page.get_by_placeholder("найдётся всё").click()
    page.get_by_placeholder("найдётся всё").fill("michael jackson")
    page.get_by_placeholder("найдётся всё").press("Enter")
    with page.expect_popup() as popup_info:
        page.get_by_role("link", name="Home - Michael Jackson Official Site").click()
        page1 = popup_info.value
  

def test_enter_to_site(page: Page):
    page.goto('https://demo.opencart.com/admin/')
    page.fill('input#input-username', 'demo')
    page.fill('input#input-password', 'demo')
    page.click('button[type=submit]')
 