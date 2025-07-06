#%%
from pathlib import Path
from PIL import Image

base = Path('.').expanduser()
sizes_and_src = {
    16: base/'favicon-16x16.png',
    32: base/'favicon-32x32.png',
    48: base/'android-chrome-192x192.png',
    64: base/'android-chrome-192x192.png',
    128: base/'android-chrome-192x192.png',
    256: base/'android-chrome-256x256.png',
}

imgs = []
for s, src in sizes_and_src.items():
    img = Image.open(src).convert('RGBA')
    if img.size[0] != s:
        img = img.resize((s, s), Image.LANCZOS)
    imgs.append(img)

imgs[0].save(
    base/'favicon.ico',
    format='ICO',
    sizes=[(s, s) for s in sizes_and_src]
)
