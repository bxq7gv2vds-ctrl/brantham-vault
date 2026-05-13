from PIL import Image, ImageDraw, ImageFont, ImageOps, ImageEnhance, ImageFilter
from pathlib import Path
import random

HERE = Path(__file__).parent
SIZE = 1080
CREAM = (239, 235, 224)
INK = (26, 26, 26)
BORDEAUX = (122, 29, 23)

# Fonts: try Newsreader, fall back to system serifs
FONT_CANDIDATES = [
    "/Users/paul/Library/Fonts/Newsreader-Regular.ttf",
    "/Users/paul/Library/Fonts/Newsreader-Italic.ttf",
    "/System/Library/Fonts/Supplemental/Georgia.ttf",
    "/System/Library/Fonts/Supplemental/Georgia Italic.ttf",
    "/System/Library/Fonts/NewYork.ttf",
]

def load_font(size, italic=False):
    for path in FONT_CANDIDATES:
        if italic and "Italic" not in path and "italic" not in path.lower():
            continue
        if not italic and ("Italic" in path or "italic" in path.lower()):
            continue
        if Path(path).exists():
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()


def cinematic_bw(img: Image.Image) -> Image.Image:
    gray = ImageOps.grayscale(img)
    gray = ImageEnhance.Contrast(gray).enhance(1.25)
    gray = ImageEnhance.Brightness(gray).enhance(0.95)
    # add subtle film grain
    grain = Image.effect_noise(gray.size, 18).convert("L")
    gray = Image.blend(gray, grain, 0.05)
    return gray


def fit_panel(path: str, panel_w: int, panel_h: int) -> Image.Image:
    src = Image.open(path).convert("RGB")
    src_ratio = src.width / src.height
    target_ratio = panel_w / panel_h
    if src_ratio > target_ratio:
        new_h = panel_h
        new_w = int(panel_h * src_ratio)
    else:
        new_w = panel_w
        new_h = int(panel_w / src_ratio)
    src = src.resize((new_w, new_h), Image.LANCZOS)
    left = (new_w - panel_w) // 2
    top = (new_h - panel_h) // 2
    src = src.crop((left, top, left + panel_w, top + panel_h))
    return cinematic_bw(src)


def tint_to_cream(img_l: Image.Image) -> Image.Image:
    # map grayscale into cream/ink tonality instead of pure b&w
    rgb = Image.new("RGB", img_l.size, CREAM)
    ink_layer = Image.new("RGB", img_l.size, INK)
    # use the grayscale as the mask: dark areas = ink, light = cream
    mask = ImageOps.invert(img_l)
    rgb.paste(ink_layer, mask=mask)
    return rgb


def draw_panel_label(canvas, x_center, y, latin_name, status):
    d = ImageDraw.Draw(canvas)
    italic_font = load_font(28, italic=True)
    regular_font = load_font(26, italic=False)

    # Latin name (italic)
    bbox = d.textbbox((0, 0), latin_name, font=italic_font)
    w = bbox[2] - bbox[0]
    d.text((x_center - w // 2, y), latin_name, font=italic_font, fill=CREAM)

    # separator
    sep_y = y + 42
    d.line([(x_center - 30, sep_y), (x_center + 30, sep_y)], fill=CREAM, width=1)

    # status
    bbox = d.textbbox((0, 0), status, font=regular_font)
    w = bbox[2] - bbox[0]
    d.text((x_center - w // 2, sep_y + 14), status, font=regular_font, fill=CREAM)


def compose():
    band_h = 180
    panel_h = SIZE - band_h
    panel_w = SIZE // 2

    canvas = Image.new("RGB", (SIZE, SIZE), CREAM)

    left = fit_panel(str(HERE / "vulture.jpg"), panel_w, panel_h)
    right = fit_panel(str(HERE / "businessman.jpg"), panel_w, panel_h)

    left_rgb = tint_to_cream(left)
    right_rgb = tint_to_cream(right)

    canvas.paste(left_rgb, (0, 0))
    canvas.paste(right_rgb, (panel_w, 0))

    # central separator
    d = ImageDraw.Draw(canvas)
    d.line([(panel_w, 0), (panel_w, panel_h)], fill=CREAM, width=2)

    # panel labels
    label_y = panel_h - 130
    draw_panel_label(canvas, panel_w // 2, label_y, "Gyps fulvus", "Espèce protégée")
    draw_panel_label(canvas, panel_w + panel_w // 2, label_y, "Repreneur PME", "Stigmatisé")

    # bottom cream band
    d.rectangle([(0, panel_h), (SIZE, SIZE)], fill=CREAM)
    # hairline above band
    d.line([(80, panel_h), (SIZE - 80, panel_h)], fill=INK, width=1)

    # main caption
    cap_font = load_font(54, italic=True)
    caption = "Même métier. Jugement opposé."
    bbox = d.textbbox((0, 0), caption, font=cap_font)
    cap_w = bbox[2] - bbox[0]
    d.text(((SIZE - cap_w) // 2, panel_h + 38), caption, font=cap_font, fill=INK)

    # brantham signature
    sig_font = load_font(20, italic=False)
    sig = "brantham partners"
    bbox = d.textbbox((0, 0), sig, font=sig_font)
    sig_w = bbox[2] - bbox[0]
    d.text((SIZE - sig_w - 40, SIZE - 36), sig, font=sig_font, fill=INK)

    out = HERE / "vautour-split-v1.jpg"
    canvas.save(out, "JPEG", quality=92)
    print(f"wrote {out}")


if __name__ == "__main__":
    compose()
