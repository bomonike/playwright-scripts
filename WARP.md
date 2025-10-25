# WARP.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

## Project Overview

This repository contains Playwright test scripts in multiple languages (Python, JavaScript, TypeScript) for browser automation testing. The primary target is testing https://the-internet.herokuapp.com demo site.

## Repository Structure

- **test-example/**: Python-based pytest-playwright examples from official Playwright documentation
- **the-internet/**: Scripts testing various controls on the-internet.herokuapp.com, supporting multiple languages (Python, JavaScript, TypeScript)

Each subdirectory maintains its own virtual environment and dependencies.

## Development Setup

### Python Scripts (test-example/ and the-internet/)

**Initial setup:**
```bash
cd test-example  # or cd the-internet
python -m venv .venv
source .venv/bin/activate
uv pip install pytest pytest-playwright playwright -U
playwright install  # Downloads Chromium, Firefox, WebKit, FFMPEG to ~/Library/Caches/ms-playwright/
```

**Cleanup:**
```bash
deactivate
rm -rf .venv .pytest_cache __pycache__
```

### JavaScript/TypeScript Scripts (the-internet/)

These use Node.js and @playwright/test framework (note the test file in the-internet/ currently doesn't have a package.json).

## Running Tests

### Python Tests with pytest
```bash
cd test-example
source .venv/bin/activate
pytest test_example.py --browser chromium --headed
```

### Python Scripts (standalone)
```bash
cd the-internet
source .venv/bin/activate
pytest flood-06-checkboxes.py --browser chromium --headed
# Or run directly:
python flood-06-checkboxes.py
```

### Run specific test function
```bash
pytest test_example.py::test_has_title --browser chromium --headed
```

## Key Technical Details

### Python Version
- Requires Python >=3.12 (per user preference for TensorFlow compatibility)
- test-example/pyproject.toml specifies `>=3.13` but should work with 3.12

### Dependencies
- **Python**: `playwright>=1.55.0`, `pytest-playwright>=0.6.0`
- Managed via pyproject.toml in test-example/
- Use `uv pip` for faster installation

### Test Configuration
- **conftest.py** enables pytest-playwright plugin: `pytest_plugins = ["pytest_playwright"]`
- Browser binaries cached at: `~/Library/Caches/ms-playwright/`

## Code Generation

Scripts in this repository were generated using:
- Playwright Codegen: `playwright codegen https://the-internet.herokuapp.com`
- AI assistance (Perplexity, etc.) with manual editing based on official Playwright documentation

## Multi-Language Support

This project intentionally includes examples in:
- **Python** with sync_playwright and pytest-playwright
- **JavaScript** using @playwright/test
- **TypeScript** (placeholder files exist)

When adding new tests, match the language pattern of the directory you're working in.

## Common Patterns

### Python Sync API
```python
from playwright.sync_api import sync_playwright, Page, expect

def test_example(page: Page):  # pytest-playwright fixture
    page.goto("https://example.com")
    expect(page).to_have_title(re.compile("Example"))
```

### Standalone Python Script
```python
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    # ... test logic
    browser.close()
```

### JavaScript/TypeScript
```javascript
const { test, expect } = require('@playwright/test');

test('description', async ({ page }) => {
    await page.goto('https://example.com');
    await expect(page.getByRole('heading')).toBeVisible();
});
```
