import json
from playwright.sync_api import sync_playwright

def login_to_eo():
    with open("config.json") as f:
        config = json.load(f)

    email = config["email"]
    password = config["password"]

    print("🔐 Logging in...")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://app.eobroker.com/")

        page.locator("input[type='email']").fill(email)
        page.locator("input[type='password']").fill(password)
        page.locator("button[type='submit']").click()

        page.wait_for_timeout(10000)
        print("✅ Logged in!")

        page.screenshot(path="live_chart.png")
        browser.close()