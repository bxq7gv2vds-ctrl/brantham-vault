import asyncio
from pathlib import Path
from playwright.async_api import async_playwright

HERE = Path(__file__).parent
FILES = [
    "post-01-top5-secteurs.html",
    "post-02-checklist-rj.html",
    "post-03-vrai-prix.html",
]

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        ctx = await browser.new_context(
            viewport={"width": 1080, "height": 1080},
            device_scale_factor=2,
        )
        page = await ctx.new_page()
        for f in FILES:
            url = f"file://{HERE / f}"
            await page.goto(url, wait_until="networkidle")
            await page.wait_for_timeout(800)
            card = page.locator(".post").first
            out = HERE / f.replace(".html", ".png")
            await card.screenshot(path=str(out), omit_background=False)
            print("rendered", out)
        await browser.close()

asyncio.run(main())
