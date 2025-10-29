
"""test_example.py here

at https://github.com/bomonike/playwright-scripts/blob/main/test_example/test_example.py

Run the sample test code posted at https://playwright.dev/python/docs/writing-tests

USAGE:
    cd test-example
    python -m venv .venv
    source .venv/bin/activate
    uv pip install pytest pytest-playwright playwright -U
    playwright install chromium  #  browser binaries: Chromium, Firefox, WebKit, FFMPEG
    # NOTE: cached in /Users/johndoe/Library/Caches/ms-playwright/ to run Playwright tests.

    pytest test_example.py --browser chromium --headed --debug

AFTER RUN:
    deactivate
    rm -rf .venv .pytest_cache __pycache__
"""
__last_change__ = "25-10-29 v002 + fix top docs :test_example.py"
__status__ = "working on macOS but browser disappears."

import re
from playwright.sync_api import Page, expect

def test_has_title(page: Page):
    page.goto("https://playwright.dev/")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Playwright"))

def test_get_started_link(page: Page):
    page.goto("https://playwright.dev/")

    # Click the get started link.
    page.get_by_role("link", name="Get started").click()

    # Expects page to have a heading with the name of Installation.
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()