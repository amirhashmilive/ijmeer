#!/usr/bin/env python3
"""
IJMEER — Cover Page Template Generator for Future Issues (Issue 3 Onwards)
Enforces ISSN placement: Right-hand top corner of cover page.

ISSN: 3139-6003 (Online ISSN)
First issue to display ISSN: Volume 1, Issue 3 (July–September 2026, Published October 2026)
"""

import os
import sys
from PIL import Image, ImageDraw, ImageFont

sys.stdout.reconfigure(encoding='utf-8')

def generate_future_cover(volume=1, issue=3, quarter_text="JULY – SEPTEMBER 2026", year=2026, output_path="scratch/cover_future_template.png"):
    """
    Generate cover page image for future IJMEER issues.
    Includes 'E-ISSN: 3139-6003' in the RIGHT-HAND TOP CORNER as mandated by ISSN India.
    """
    W, H = 1242, 1856
    img = Image.new("RGB", (W, H), color=(8, 8, 8))
    draw = ImageDraw.Draw(img)

    GOLD_MAIN = (212, 175, 55)
    GOLD_LIGHT = (235, 205, 110)
    GOLD_DARK = (165, 130, 30)

    margin_outer = 45
    margin_inner = 60

    draw.rectangle([margin_outer, margin_outer, W - margin_outer, H - margin_outer], outline=GOLD_MAIN, width=4)
    draw.rectangle([margin_inner, margin_inner, W - margin_inner, H - margin_inner], outline=GOLD_DARK, width=2)

    font_title = font_logo = font_medium = font_small = font_issn = None
    font_paths = [
        "C:\\Windows\\Fonts\\georgia.ttf",
        "C:\\Windows\\Fonts\\times.ttf",
        "C:\\Windows\\Fonts\\arial.ttf"
    ]

    for fp in font_paths:
        if os.path.exists(fp):
            try:
                font_title = ImageFont.truetype(fp, 46)
                font_logo = ImageFont.truetype(fp, 110)
                font_medium = ImageFont.truetype(fp, 42)
                font_small = ImageFont.truetype(fp, 32)
                font_issn = ImageFont.truetype(fp, 30)
                break
            except Exception:
                pass

    if not font_issn:
        font_title = font_logo = font_medium = font_small = font_issn = ImageFont.load_default()

    # 1. MANDATORY ISSN PLACEMENT — RIGHT-HAND TOP CORNER
    issn_text = "E-ISSN: 3139-6003"
    issn_x = W - margin_inner - 20
    issn_y = margin_inner + 25

    bbox = draw.textbbox((0, 0), issn_text, font=font_issn)
    text_w = bbox[2] - bbox[0]
    draw.text((issn_x - text_w, issn_y), issn_text, fill=GOLD_LIGHT, font=font_issn)

    # 2. JOURNAL TITLE
    line1 = "INTERNATIONAL JOURNAL OF"
    line2 = "MULTIDISCIPLINARY"
    line3 = "EXPLICATION AND"
    line4 = "EMERGING RESEARCH"

    y_title = 220
    for l in [line1, line2, line3, line4]:
        tb = draw.textbbox((0, 0), l, font=font_title)
        lw = tb[2] - tb[0]
        draw.text(((W - lw) / 2, y_title), l, fill=GOLD_LIGHT, font=font_title)
        y_title += 60

    # 3. JOURNAL LOGO
    logo_text = "IJMEER"
    tb = draw.textbbox((0, 0), logo_text, font=font_logo)
    lw = tb[2] - tb[0]
    draw.text(((W - lw) / 2, 620), logo_text, fill=GOLD_MAIN, font=font_logo)

    # 4. VOLUME & ISSUE & QUARTER
    vol_text = f"VOLUME {volume} | ISSUE {issue}"
    tb = draw.textbbox((0, 0), vol_text, font=font_medium)
    lw = tb[2] - tb[0]
    draw.text(((W - lw) / 2, 850), vol_text, fill=GOLD_LIGHT, font=font_medium)

    tb = draw.textbbox((0, 0), quarter_text, font=font_medium)
    lw = tb[2] - tb[0]
    draw.text(((W - lw) / 2, 920), quarter_text, fill=GOLD_LIGHT, font=font_medium)

    # 5. FOOTER FEATURES
    feat1 = "PEER REVIEWED | OPEN ACCESS"
    feat2 = "QUARTERLY"
    tb = draw.textbbox((0, 0), feat1, font=font_small)
    lw = tb[2] - tb[0]
    draw.text(((W - lw) / 2, 1120), feat1, fill=GOLD_LIGHT, font=font_small)

    tb = draw.textbbox((0, 0), feat2, font=font_small)
    lw = tb[2] - tb[0]
    draw.text(((W - lw) / 2, 1170), feat2, fill=GOLD_LIGHT, font=font_small)

    year_str = str(year)
    tb = draw.textbbox((0, 0), year_str, font=font_medium)
    lw = tb[2] - tb[0]
    draw.text(((W - lw) / 2, 1270), year_str, fill=GOLD_MAIN, font=font_medium)

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    img.save(output_path)
    print(f"Generated Future Issue Cover Template: {output_path}")

if __name__ == "__main__":
    generate_future_cover(volume=1, issue=3, quarter_text="JULY – SEPTEMBER 2026", year=2026)
