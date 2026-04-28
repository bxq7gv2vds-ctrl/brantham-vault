"""Render all HTML templates to PNG (retina @2x).

Usage:
  python3 render.py                # tous formats
  python3 render.py 1080x1080      # un seul format
"""
import asyncio
import sys
from pathlib import Path
from playwright.async_api import async_playwright

ROOT = Path(__file__).parent

FORMATS = {
    "1080x1080": (1080, 1080),
    "1080x1350": (1080, 1350),
    "1200x628":  (1200, 628),
    "1920x1080": (1920, 1080),
}

async def render_format(browser, fmt, w, h):
    folder = ROOT / f"templates-{fmt}"
    if not folder.exists():
        return
    files = sorted([p for p in folder.glob("*.html") if not p.name.startswith("_")])
    if not files:
        return
    ctx = await browser.new_context(
        viewport={"width": w, "height": h},
        device_scale_factor=2,
    )
    page = await ctx.new_page()
    for f in files:
        await page.goto(f"file://{f}", wait_until="networkidle")
        await page.wait_for_timeout(900)
        out = f.with_suffix(".png")
        await page.locator(".post").first.screenshot(path=str(out))
        print(f"  rendered {fmt}/{out.name}")
    await ctx.close()

async def main():
    target = sys.argv[1] if len(sys.argv) > 1 else None
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        for fmt, (w, h) in FORMATS.items():
            if target and target != fmt:
                continue
            print(f"[{fmt}]")
            await render_format(browser, fmt, w, h)
        await browser.close()

asyncio.run(main())
