"""Vautour split panel — DA Brantham (Anakin reference).

Layout 1080x1080:
  - cream bg #efebe0
  - inner image grid 960x960, centered, top 40px
  - 2 cells side by side (480x960 each)
  - Impact white text + 1.8px black stroke, bottom-center per cell
  - Brantham logo navy, centered bottom 24px
"""
from PIL import Image, ImageDraw, ImageFont, ImageOps
from pathlib import Path

HERE = Path(__file__).parent
SIZE = 1080
CREAM = (239, 235, 224)
NAVY = (14, 26, 43)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

GRID_TOP = 40
GRID_W = 960
GRID_H = 960
GRID_LEFT = (SIZE - GRID_W) // 2

IMPACT = "/System/Library/Fonts/Supplemental/Impact.ttf"
ARIAL_NARROW_BOLD = "/System/Library/Fonts/Supplemental/Arial Narrow Bold.ttf"


def load_impact(size):
    for path in (IMPACT, ARIAL_NARROW_BOLD):
        if Path(path).exists():
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()


def fit_cell(path: str, w: int, h: int) -> Image.Image:
    src = Image.open(path).convert("RGB")
    src_ratio = src.width / src.height
    target_ratio = w / h
    if src_ratio > target_ratio:
        new_h = h
        new_w = int(h * src_ratio)
    else:
        new_w = w
        new_h = int(w / src_ratio)
    src = src.resize((new_w, new_h), Image.LANCZOS)
    left = (new_w - w) // 2
    top = (new_h - h) // 2
    return src.crop((left, top, left + w, top + h))


def draw_meme_text(draw, text, center_x, baseline_y, font, stroke_w=4, stroke_fill=BLACK, fill=WHITE):
    """Anakin-style: white fill, thick black stroke, centered."""
    bbox = draw.textbbox((0, 0), text, font=font, stroke_width=stroke_w)
    w = bbox[2] - bbox[0]
    h = bbox[3] - bbox[1]
    x = center_x - w // 2 - bbox[0]
    y = baseline_y - h - bbox[1]
    draw.text(
        (x, y),
        text,
        font=font,
        fill=fill,
        stroke_width=stroke_w,
        stroke_fill=stroke_fill,
    )


def compose(left_path, right_path, left_text, right_text, out_name, caption=None):
    canvas = Image.new("RGB", (SIZE, SIZE), CREAM)

    cell_w = GRID_W // 2
    cell_h = GRID_H

    left_img = fit_cell(left_path, cell_w, cell_h)
    right_img = fit_cell(right_path, cell_w, cell_h)

    canvas.paste(left_img, (GRID_LEFT, GRID_TOP))
    canvas.paste(right_img, (GRID_LEFT + cell_w, GRID_TOP))

    d = ImageDraw.Draw(canvas)

    # Impact uppercase white with black stroke (Anakin style)
    font_main = load_impact(64)

    # padding bottom in cell: 28px
    baseline = GRID_TOP + cell_h - 36

    draw_meme_text(d, left_text, GRID_LEFT + cell_w // 2, baseline, font_main, stroke_w=4)
    draw_meme_text(d, right_text, GRID_LEFT + cell_w + cell_w // 2, baseline, font_main, stroke_w=4)

    # optional caption above the logo
    if caption:
        font_cap = load_impact(34)
        cap_y_baseline = SIZE - 78
        bbox = d.textbbox((0, 0), caption, font=font_cap)
        w = bbox[2] - bbox[0]
        d.text(((SIZE - w) // 2, cap_y_baseline - (bbox[3] - bbox[1])), caption,
               font=font_cap, fill=NAVY)

    # Brantham logo navy at bottom-center, height 38px
    logo_path = HERE / "logo.png"
    if logo_path.exists():
        logo = Image.open(logo_path).convert("RGBA")
        target_h = 38
        ratio = target_h / logo.height
        target_w = int(logo.width * ratio)
        logo = logo.resize((target_w, target_h), Image.LANCZOS)
        # paste with alpha
        canvas.paste(logo, ((SIZE - target_w) // 2, SIZE - target_h - 24), logo)

    out = HERE / out_name
    canvas.save(out, "JPEG", quality=92)
    print(f"wrote {out}")


if __name__ == "__main__":
    # v2: pure Anakin DA, no caption, contrast does the work
    compose(
        left_path=str(HERE / "vulture_b.jpg"),
        right_path=str(HERE / "businessman.jpg"),
        left_text="ESPÈCE PROTÉGÉE",
        right_text="STIGMATISÉ",
        out_name="vautour-split-v2.jpg",
    )

    # v3: with central caption above the logo
    compose(
        left_path=str(HERE / "vulture_b.jpg"),
        right_path=str(HERE / "businessman.jpg"),
        left_text="ESPÈCE PROTÉGÉE",
        right_text="STIGMATISÉ",
        out_name="vautour-split-v3.jpg",
        caption="MÊME MÉTIER. JUGEMENT OPPOSÉ.",
    )
