# WARP.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

## Project Overview

This is a collection of Playwright test scripts organized by target application/website. The repository contains browser automation tests written in both JavaScript and TypeScript.

## Repository Structure

- `aws/` - Playwright scripts for AWS-related testing (currently placeholder files)
- `the-internet/` - Test scripts targeting https://the-internet.herokuapp.com
  - Scripts use naming convention: `AE##_<TestName>_<metadata>.{js,ts}`
  - Example: `AE06_CheckBox.js` for checkbox interaction tests

## Commands

Since this repository does not have a package.json or configuration files yet, tests must be run using a globally installed Playwright or a parent project's Playwright installation.

**Run a specific test:**
```bash
npx playwright test the-internet/AE06_CheckBox.js
```

**Run tests in a directory:**
```bash
npx playwright test the-internet/
```

**Run tests in headed mode (see browser):**
```bash
npx playwright test --headed the-internet/AE06_CheckBox.js
```

**Run tests in debug mode:**
```bash
npx playwright test --debug the-internet/AE06_CheckBox.js
```

## Development Guidelines

### File Naming
- Test files follow the pattern: `AE##_<DescriptiveName>_<optionalMetadata>.{js,ts}`
- Use descriptive names that indicate what is being tested
- The `AE##` prefix appears to be a numbering system for organizing tests

### Test Structure
- Tests use Playwright's test runner: `const { test, expect } = require('@playwright/test')`
- Each test file should focus on a specific feature or interaction
- Use locators with `page.getByRole()` or `page.locator()` for element selection
- Prefer semantic selectors (role, text) over CSS/XPath when possible

### Adding New Tests
When creating new test files:
1. Place them in the appropriate directory (`aws/` or `the-internet/`)
2. Follow the `AE##_` naming convention
3. Use either `.js` or `.ts` extension (both are supported)
4. Import Playwright test utilities at the top
5. Target https://the-internet.herokuapp.com for `the-internet/` directory tests

### TypeScript vs JavaScript
- Both `.js` and `.ts` files are used in this repository
- For JavaScript files, use `// @ts-check` comment at the top for type checking
- Maintain consistency within each directory when possible
