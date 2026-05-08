import asyncio
from pathlib import Path
from playwright.async_api import async_playwright

HERE = Path(__file__).parent
TPL = HERE / "templates"

FILES = [
    "funnel-lp.html",
    "dispositif-lp.html",
]

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        for variant_class, suffix in [("", ""), ("dark", "-navy")]:
            for f in FILES:
                ctx = await browser.new_context(
                    viewport={"width": 1080, "height": 1080},
                    device_scale_factor=2,
                )
                page = await ctx.new_page()
                url = f"file://{TPL / f}"
                await page.goto(url, wait_until="networkidle")
                if variant_class:
                    await page.evaluate(f"document.querySelector('.post').classList.add('{variant_class}')")
                    await page.wait_for_timeout(300)
                await page.wait_for_timeout(600)
                card = page.locator(".post").first
                out = HERE / f.replace(".html", f"{suffix}.png")
                await card.screenshot(path=str(out), omit_background=False)
                print("rendered", out.name)
                await ctx.close()
        await browser.close()

asyncio.run(main())
