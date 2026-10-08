import { test, expect } from '@playwright/test';

// Real browser test against the running API (F-52 fix: the old spec asserted only that <body> exists).
// Needs: the API running at baseURL and E2E_TOKEN set to a dispatcher token (scripts/issue_dev_token.py).
test('dispatcher can list, open, summarise and decide', async ({ page }) => {
  const token = process.env.E2E_TOKEN; // secret-scan: allow (env lookup, no literal)
  test.skip(!token, 'E2E_TOKEN not set');
  await page.goto('/ops/');
  await page.getByLabel('Bearer token').fill(token!);
  await page.getByRole('button', { name: 'Load shipments' }).click();
  await page.getByLabel('Status').selectOption('exception');
  const first = page.locator('#list tbody tr').first();
  await expect(first).toBeVisible();
  await first.click();
  await expect(page.locator('#record dd').first()).not.toBeEmpty();
  await page.getByRole('button', { name: 'Summarize exception' }).click();
  await expect(page.getByText('Suggestion only. A person must decide.')).toBeVisible();
  await page.getByRole('button', { name: 'Approve suggestion' }).click();
  await expect(page.locator('#decision')).toContainText('Recorded:');
});
