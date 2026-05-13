"""Vautour split panel v4 — DA Brantham (Anakin reference), texte renforcé."""
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from pathlib import Path

HERE = Path(__file__).parent
SIZE = 1080
CREAM = (239, 235, 224)
NAVY = (14, 26, 43)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

GRID_TOP = 56
GRID_W = 960
GRID_H = 924
GRID_LEFT = (SIZE - GRID_W) // 2
GUTTER = 10

IMPACT = "/System/Library/Fonts/Supplemental/Impact.ttf"


def load_impact(size):
    return ImageFont.truetype(IMPACT, size)


def fit_cell(path: str, w: int, h: int) -> Image.Image:
    src = Image.open(path).convert("RGB")
    sr = src.width / src.height
    tr = w / h
    if sr > tr:
        new_h = h
        new_w = int(h * sr)
    else:
        new_w = w
        new_h = int(w / sr)
    src = src.resize((new_w, new_h), Image.LANCZOS)
    left = (new_w - w) // 2
    top = (new_h - h) // 2
    return src.crop((left, top, left + w, top + h))


def add_bottom_vignette(img: Image.Image, fade_h_ratio=0.42, max_alpha=170) -> Image.Image:
    """Soft black gradient on the bottom half so meme text pops everywhere."""
    w, h = img.size
    fade_h = int(h * fade_h_ratio)
    overlay = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    px = overlay.load()
    for y in range(h - fade_h, h):
        t = (y - (h - fade_h)) / fade_h
        a = int((t ** 1.8) * max_alpha)
        for x in range(w):
            px[x, y] = (0, 0, 0, a)
    base = img.convert("RGBA")
    return Image.alpha_composite(base, overlay).convert("RGB")


def draw_meme_text(canvas: Image.Image, text: str, center_x: int, baseline_y: int,
                   font_size=84, stroke_w=7, glow_blur=14, glow_alpha=220):
    """Anakin-style multi-layer text: glow + thick stroke + white fill."""
    font = load_impact(font_size)

    # Render text on a transparent layer first to apply blur for glow
    tmp = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
    td = ImageDraw.Draw(tmp)

    # Measure
    bbox = td.textbbox((0, 0), text, font=font, stroke_width=stroke_w)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    x = center_x - tw // 2 - bbox[0]
    y = baseline_y - th - bbox[1]

    # Glow pass: solid black, then heavy blur
    glow_layer = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
    gd = ImageDraw.Draw(glow_layer)
    gd.text((x, y), text, font=font, fill=(0, 0, 0, glow_alpha),
            stroke_width=stroke_w + 4, stroke_fill=(0, 0, 0, glow_alpha))
    glow_layer = glow_layer.filter(ImageFilter.GaussianBlur(glow_blur))

    base = canvas.convert("RGBA")
    base = Image.alpha_composite(base, glow_layer)

    # Stroke + fill pass on the actual canvas
    final = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
    fd = ImageDraw.Draw(final)
    fd.text((x, y), text, font=font, fill=(255, 255, 255, 255),
            stroke_width=stroke_w, stroke_fill=(0, 0, 0, 255))
    base = Image.alpha_composite(base, final)

    return base.convert("RGB")


def fit_size(text, target_w, max_size=110, min_size=44, stroke_w=7):
    """Reduce font size until rendered width fits target_w."""
    tmp = Image.new("RGBA", (10, 10))
    d = ImageDraw.Draw(tmp)
    size = max_size
    while size >= min_size:
        font = load_impact(size)
        bbox = d.textbbox((0, 0), text, font=font, stroke_width=stroke_w)
        if (bbox[2] - bbox[0]) <= target_w:
            return size
        size -= 2
    return min_size


def compose(left_path, right_path, left_text, right_text, out_name):
    canvas = Image.new("RGB", (SIZE, SIZE), CREAM)

    cell_w = (GRID_W - GUTTER) // 2
    cell_h = GRID_H

    left_img = fit_cell(left_path, cell_w, cell_h)
    right_img = fit_cell(right_path, cell_w, cell_h)

    left_img = add_bottom_vignette(left_img)
    right_img = add_bottom_vignette(right_img)

    canvas.paste(left_img, (GRID_LEFT, GRID_TOP))
    canvas.paste(right_img, (GRID_LEFT + cell_w + GUTTER, GRID_TOP))

    # auto-fit: both texts share the same size for visual coherence
    text_target_w = int(cell_w * 0.86)
    common = min(
        fit_size(left_text, text_target_w),
        fit_size(right_text, text_target_w),
    )

    # text baselines: 56px above cell bottom
    baseline = GRID_TOP + cell_h - 56

    canvas = draw_meme_text(
        canvas, left_text,
        GRID_LEFT + cell_w // 2, baseline,
        font_size=common, stroke_w=7, glow_blur=14,
    )
    canvas = draw_meme_text(
        canvas, right_text,
        GRID_LEFT + cell_w + GUTTER + cell_w // 2, baseline,
        font_size=common, stroke_w=7, glow_blur=14,
    )

    # Brantham logo navy at bottom
    logo_path = HERE / "logo.png"
    if logo_path.exists():
        logo = Image.open(logo_path).convert("RGBA")
        target_h = 44
        ratio = target_h / logo.height
        target_w = int(logo.width * ratio)
        logo = logo.resize((target_w, target_h), Image.LANCZOS)
        canvas.paste(logo, ((SIZE - target_w) // 2, SIZE - target_h - 26), logo)

    out = HERE / out_name
    canvas.save(out, "JPEG", quality=94)
    print(f"wrote {out}")


if __name__ == "__main__":
    pairs = [
        ("ESPÈCE PROTÉGÉE", "STIGMATISÉ", "vautour-split-v5a.jpg"),
        ("PROTÉGÉ", "STIGMATISÉ", "vautour-split-v5b.jpg"),
        ("INDISPENSABLE", "MÉPRISÉ", "vautour-split-v5c.jpg"),
    ]
    for left, right, name in pairs:
        compose(
            left_path=str(HERE / "vulture_b.jpg"),
            right_path=str(HERE / "businessman.jpg"),
            left_text=left,
            right_text=right,
            out_name=name,
        )
