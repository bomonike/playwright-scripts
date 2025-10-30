#!/usr/bin/env python3
# /// script
# requires-python = ">=3.12"
# dependencies = [
#   "playwright",
#   "pytest-playwright",
# ]
# ///

"""test_menus.py here

at https://github.com/bomonike/playwright-scripts/blob/main/the-internet/test_menus.py

Test script for visiting all example links on the-internet.herokuapp.com.
Described at https://wilsonmar.github.io/flood-the-internet/

USAGE:
    git clone https://github.com/bomonike/playwright-scripts --depth 1
    cd flood-the-internet/the-internet
    python -m venv .venv
    source .venv/bin/activate
    uv pip install pytest pytest-playwright playwright -U
    playwright install  #  browser binaries: Chromium, Firefox, WebKit, FFMPEG
    # NOTE: cached in /Users/johndoe/Library/Caches/ms-playwright/ to run Playwright tests.

    pytest test_menus.py --browser chromium --headed
    deactivate
    rm -rf .venv .pytest_cache __pycache__
"""

__last_change__ = "25-10-29 v004 + fix urls :test_menus.py"
__status__ = "working on macOS but browser disappears."

from playwright.sync_api import Page, expect

BASE_URL = "https://the-internet.herokuapp.com"

def test_visit_each_example(page: Page):
    """Visit each example link on the homepage."""
    page.goto(BASE_URL)
    links = page.query_selector_all('ul li a')
    
    # Extract link data before navigation
    link_data = []
    for link in links:
        text = link.inner_text()
        href = link.get_attribute('href')
        if href:
            link_data.append((text, href))
    
    print(f"Found {len(link_data)} example links.")

    for link_text, href in link_data:
        # Skip endpoints that require authentication
        if '/basic_auth' in href or '/digest_auth' in href or '/download_secure' in href:
            print(f"Skipping: {link_text} ({href}) - requires authentication")
            continue
        
        print(f"Visiting: {link_text} ({href})")
        page.goto(f"{BASE_URL}{href}")
        page.wait_for_timeout(500)  # Human-like pause
