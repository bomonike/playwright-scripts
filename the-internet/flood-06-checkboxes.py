#!/usr/bin/env python3
# /// script
# requires-python = ">=3.13"
# dependencies = [
#   "sync_playwright",
# ]
# ///

"""flood-06-checkboxes.py here.

https://wilsonmar.github.io/flood-the-internet/

USAGE:
    cd the-internet
    python -m venv .venv
    source .venv/bin/activate
    uv pip install pytest pytest-playwright playwright -U
    playwright install  #  browser binaries: Chromium, Firefox, WebKit, FFMPEG
    # NOTE: cached in /Users/johndoe/Library/Caches/ms-playwright/ to run Playwright tests.

    pytest flood-06-checkboxes.py --browser chromium --headed

"""

from playwright.sync_api import sync_playwright

def test_click_checkboxes():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://the-internet.herokuapp.com/checkboxes")
        
        # Select all checkbox elements on the page
        checkboxes = page.locator("input[type='checkbox']")
        
        # Click each checkbox to toggle it
        count = checkboxes.count()
        for i in range(count):
            checkboxes.nth(i).check()
        
        # Optional: Keep the browser open to view result
        # input("Press Enter to close browser...")
        browser.close()

if __name__ == "__main__":
    test_click_checkboxes()
