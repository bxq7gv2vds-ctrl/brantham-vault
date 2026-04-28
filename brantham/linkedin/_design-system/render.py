"""Render all HTML templates to PNG (retina @2x) — light + navy variants.

Usage:
  python3 render.py                # tous formats, light + navy
  python3 render.py 1080x1080      # un seul format
  python3 render.py --light-only   # skipper navy
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

async def render_one(page, html_file, dark=False):
    await page.goto(f"file://{html_file}", wait_until="networkidle")
    if dark:
        await page.evaluate("document.querySelector('.post').classList.add('dark')")
        await page.wait_for_timeout(700)
        suffix = "-navy"
    else:
        await page.wait_for_timeout(700)
        suffix = ""
    out = html_file.with_name(html_file.stem + suffix + ".png")
    await page.locator(".post").first.screenshot(path=str(out))
    print(f"  rendered {html_file.parent.name}/{out.name}")

async def render_format(browser, fmt, w, h, light_only=False):
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
        await render_one(page, f, dark=False)
        if not light_only:
            await render_one(page, f, dark=True)
    await ctx.close()

async def main():
    args = sys.argv[1:]
    light_only = "--light-only" in args
    args = [a for a in args if not a.startswith("--")]
    target = args[0] if args else None

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        for fmt, (w, h) in FORMATS.items():
            if target and target != fmt:
                continue
            print(f"[{fmt}]")
            await render_format(browser, fmt, w, h, light_only=light_only)
        await browser.close()

asyncio.run(main())
