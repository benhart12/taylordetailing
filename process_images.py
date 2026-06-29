"""Clean up Taylor Detailing photos: fix orientation, crop distracting
background clutter, enhance color/contrast/brightness, and export
web-optimized sizes into ./images.
"""
import os
from PIL import Image, ImageOps, ImageEnhance

SRC = "."
OUT = "images"
os.makedirs(OUT, exist_ok=True)


def load(name):
    return ImageOps.exif_transpose(Image.open(os.path.join(SRC, name))).convert("RGB")


def crop_frac(im, left=0.0, top=0.0, right=1.0, bottom=1.0):
    w, h = im.size
    return im.crop((int(w * left), int(h * top), int(w * right), int(h * bottom)))


def enhance(im, brightness=1.0, contrast=1.0, color=1.0, sharpness=1.0):
    if brightness != 1.0:
        im = ImageEnhance.Brightness(im).enhance(brightness)
    if contrast != 1.0:
        im = ImageEnhance.Contrast(im).enhance(contrast)
    if color != 1.0:
        im = ImageEnhance.Color(im).enhance(color)
    if sharpness != 1.0:
        im = ImageEnhance.Sharpness(im).enhance(sharpness)
    return im


def save(im, name, max_w=1600, quality=82):
    if im.width > max_w:
        h = int(im.height * max_w / im.width)
        im = im.resize((max_w, h), Image.LANCZOS)
    path = os.path.join(OUT, name)
    im.save(path, "JPEG", quality=quality, optimize=True, progressive=True)
    print(f"{name}: {im.size}  {os.path.getsize(path)//1024} KB")


# --- Per-image recipes -------------------------------------------------------

# White Lincoln SUV exterior. Silver car + orange hose clutter on the right.
im = load("IMG_5304.jpeg")
im = crop_frac(im, left=0.0, top=0.04, right=0.74, bottom=1.0)
im = enhance(im, brightness=1.05, contrast=1.08, color=1.12, sharpness=1.15)
save(im, "lincoln-exterior.jpg")

# Black Audi Q5 exterior. Good shot; trim leafy foreground a touch.
im = load("IMG_6634.jpeg")
im = crop_frac(im, left=0.0, top=0.0, right=1.0, bottom=0.92)
im = enhance(im, brightness=1.06, contrast=1.1, color=1.12, sharpness=1.15)
save(im, "audi-exterior.jpg")

# Gray Honda CR-V in garage. Crop the cluttered left wall / ceiling.
im = load("IMG_6967.jpeg")
im = crop_frac(im, left=0.05, top=0.18, right=1.0, bottom=1.0)
im = enhance(im, brightness=1.12, contrast=1.08, color=1.12, sharpness=1.15)
save(im, "crv-exterior.jpg")

# Light-blue Miata exterior. Tighten onto the car, drop messy house/yard edges.
im = load("IMG_6293.jpeg")
im = crop_frac(im, left=0.06, top=0.22, right=0.96, bottom=0.98)
im = enhance(im, brightness=1.05, contrast=1.1, color=1.15, sharpness=1.15)
save(im, "miata-exterior.jpg")

# RAV4 tan leather interior.
im = load("IMG_5080.jpeg")
im = crop_frac(im, left=0.02, top=0.02, right=0.98, bottom=0.98)
im = enhance(im, brightness=1.08, contrast=1.06, color=1.12, sharpness=1.12)
save(im, "rav4-interior.jpg")

# Lincoln light interior, shot in low light -> lift brightness.
im = load("IMG_5292.jpeg")
im = crop_frac(im, left=0.02, top=0.02, right=0.98, bottom=0.98)
im = enhance(im, brightness=1.18, contrast=1.08, color=1.1, sharpness=1.12)
save(im, "lincoln-interior.jpg")

print("done")
