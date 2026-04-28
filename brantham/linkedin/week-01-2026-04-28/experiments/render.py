import asyncio
from pathlib import Path
from playwright.async_api import async_playwright

HERE = Path(__file__).parent

async def main():
    files = sorted([p for p in HERE.glob("*.html")])
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        ctx = await browser.new_context(
            viewport={"width": 1080, "height": 1080},
            device_scale_factor=2,
        )
        page = await ctx.new_page()
        for f in files:
            await page.goto(f"file://{f}", wait_until="networkidle")
            await page.wait_for_timeout(900)
            out = f.with_suffix(".png")
            await page.locator(".post").first.screenshot(path=str(out))
            print(f"rendered {out.name}")
        await browser.close()

asyncio.run(main())
