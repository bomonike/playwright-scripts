# playwright-scripts/README.md

## Install
1. In a Terminal, navigate to a folder 
1. git clone https://github.com/bomonike/playwright-scripts; cd playwright-scripts
1. Create WARP.md
```
    cd test-example
    python -m venv .venv
    source .venv/bin/activate
    uv pip install pytest pytest-playwright playwright -U
    playwright install  #  browser binaries: Chromium, Firefox, WebKit, FFMPEG
    # NOTE: cached in /Users/johndoe/Library/Caches/ms-playwright/ to run Playwright tests.

    pytest test_example.py --browser chromium --headed

RESULT: By default pytest runs tests on chromium:
platform darwin -- Python 3.12.11, pytest-8.4.2, pluggy-1.6.0
rootdir: /Users/johndoe/bomonike/playwright-scripts
configfile: pyproject.toml
plugins: base-url-2.1.0, playwright-0.7.1
collected 2 items
test_example.py ..     

# Use https://playwright.dev/python/docs/trace-viewer

    playwright show-trace trace.zip
    playwright show-trace test-results/tests-test-example-py-test-has-title-chromium/trace.zip
    playwright show-trace test-results/tests-test-example-py-test-get-started-link-chromium/trace.zip
```

## Target URL

https://the-internet.herokuapp.com

demo.playwright.dev/todomvc

## Creating scripts in Python

https://playwright.dev/python/docs/codegen
Playwright Inspector to generate test scripts.

playwright codegen https://the-internet.herokuapp.com

works from VSCode 

## Extensions

https://www.perplexity.ai/search/write-an-app-that-navigates-th-GQK4OCCATHGFI2H9V7EhHg#0