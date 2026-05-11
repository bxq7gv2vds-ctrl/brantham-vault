import asyncio
from pathlib import Path
from playwright.async_api import async_playwright

HERE = Path(__file__).parent

# (file, viewport_width, viewport_height)
FILES = [
    ("post-02-A-signal.html", 1080, 1080),
    ("post-05-V1-pyramide.html", 1080, 1080),
    ("post-05-V2-verrou.html", 1080, 1080),
    ("post-05-V3-chronologie.html", 1080, 1080),
    ("post-05-V4-resultat.html", 1080, 1080),
]

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        for f, w, h in FILES:
            ctx = await browser.new_context(
                viewport={"width": w, "height": h},
                device_scale_factor=2,
            )
            page = await ctx.new_page()
            url = f"file://{HERE / f}"
            await page.goto(url, wait_until="networkidle")
            await page.wait_for_timeout(800)
            card = page.locator(".post").first
            out = HERE / f.replace(".html", ".png")
            await card.screenshot(path=str(out), omit_background=False)
            print("rendered", out)
            await ctx.close()
        await browser.close()

asyncio.run(main())
