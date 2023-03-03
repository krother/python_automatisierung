
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.virustotal.com/gui/")
    page.goto("https://www.virustotal.com/gui/home/upload")
    page.get_by_role("button", name="Choose file").click()
    page.get_by_role("button", name="Choose file").set_input_files("/home/kristian/projects/python_automatisierung/codebeispiele/web/automatisierungpizza.txt")
    page.locator("[data-test=\"confirm-upload\"]").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
