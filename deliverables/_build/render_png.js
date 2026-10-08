// Render diagrams/*.svg to PNG at 2x with headless Chromium. Usage: node deliverables/_build/render_png.js
const { chromium } = require("playwright");
const fs = require("fs");
const path = require("path");

(async () => {
  const dir = path.join(__dirname, "..", "diagrams");
  const browser = await chromium.launch({ executablePath: fs.existsSync("/opt/pw-browsers/chromium") ? undefined : undefined });
  const page = await browser.newPage({ deviceScaleFactor: 2 });
  for (const f of fs.readdirSync(dir).filter((x) => x.endsWith(".svg"))) {
    const svg = fs.readFileSync(path.join(dir, f), "utf8");
    const m = svg.match(/width="(\d+)" height="(\d+)"/);
    await page.setViewportSize({ width: +m[1], height: +m[2] });
    await page.setContent(`<html><body style="margin:0">${svg}</body></html>`);
    await page.screenshot({ path: path.join(dir, f.replace(".svg", ".png")), clip: { x: 0, y: 0, width: +m[1], height: +m[2] } });
  }
  await browser.close();
  console.log("png done");
})();
