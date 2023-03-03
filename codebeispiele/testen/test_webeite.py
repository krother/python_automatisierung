
from playwright.sync_api import sync_playwright
import re


def test_python_kommt_auf_der_webseite_vor():
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.academis.eu")
        page.is_visible('#headline')

        html = page.inner_html('#headline')
        print(html)
        assert re.search("python", html, re.IGNORECASE)
