// @ts-check
const { test, expect } = require('@playwright/test');

test('clicking check boxes', async ({ page }) => {
  await page.goto('https://the-internet.herokuapp.com/checkboxes');

  await expect(page.getByRole('heading', { name: 'Checkboxes' })).toBeVisible();
  const checkboxForm = await page.locator('#checkboxes');

  // Check the first checkbox using the checkboxForm locator
  await checkboxForm.locator('input[type="checkbox"]').first().check();
  // unCheck the second checkbox using the checkboxForm locator
  await checkboxForm.locator('input[type="checkbox"]').nth(1).uncheck();
});

