"""Render pitch-deck HTML files to PNG (retina @2x).

Usage:
  python3 render.py            # tous les .html du dossier
  python3 render.py 01-cover   # un seul fichier (par stem)
"""
import asyncio
import sys
from pathlib import Path
from playwright.async_api import async_playwright

ROOT = Path(__file__).parent
W, H = 1920, 1080


async def render_one(page, html_file):
    await page.goto(f"file://{html_file}", wait_until="networkidle")
    await page.wait_for_timeout(800)
    out = html_file.with_suffix(".png")
    await page.locator(".post").first.screenshot(path=str(out))
    print(f"  rendered {out.name}")


async def main():
    target = sys.argv[1] if len(sys.argv) > 1 else None
    files = sorted(ROOT.glob("*.html"))
    if target:
        files = [f for f in files if f.stem == target or f.name == target]

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        ctx = await browser.new_context(viewport={"width": W, "height": H},
                                        device_scale_factor=2)
        page = await ctx.new_page()
        for f in files:
            await render_one(page, f)
        await ctx.close()
        await browser.close()


if __name__ == "__main__":
    asyncio.run(main())
