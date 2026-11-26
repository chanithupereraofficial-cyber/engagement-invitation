from PIL import Image, ImageFilter
import numpy as np

src_path = 'C:/Users/User/.gemini/antigravity/brain/a399d581-13bd-4534-9cd3-82439039c61b/.user_uploaded/media_1795573038330_b8d2c615.png'
dest_path = 'C:/Users/User/.gemini/antigravity/scratch/wedding-invitation/assets/weddingRings.png'

img = Image.open(src_path).convert('RGBA')
arr = np.array(img, dtype=np.float32)

r = arr[:, :, 0]
g = arr[:, :, 1]
b = arr[:, :, 2]

# Measure background color in multiple border points
bg_samples = np.concatenate([
    arr[:15, :15, :3].reshape(-1, 3),
    arr[:15, -15:, :3].reshape(-1, 3),
    arr[-15:, :15, :3].reshape(-1, 3),
    arr[-15:, -15:, :3].reshape(-1, 3),
])
bg_color = np.median(bg_samples, axis=0)
print(f"Sampled BG color: {bg_color}")

diff = np.sqrt(np.sum((arr[:, :, :3] - bg_color)**2, axis=2))

# Smooth alpha calculation with soft falloff so line edges are clean
# and all background is 100% transparent (alpha = 0)
alpha = np.clip((diff - 12.0) / (32.0 - 12.0), 0.0, 1.0) * 255.0

# Deepen the gold color:
# Gold has high red and yellow (R > G >> B)
# Let's boost vibrancy and warm gold richness:
out_arr = np.zeros_like(arr, dtype=np.uint8)

r_enhanced = np.clip(r * 1.10, 0, 255)
g_enhanced = np.clip(g * 1.03, 0, 255)
b_enhanced = np.clip(b * 0.75, 0, 255)

out_arr[:, :, 0] = r_enhanced.astype(np.uint8)
out_arr[:, :, 1] = g_enhanced.astype(np.uint8)
out_arr[:, :, 2] = b_enhanced.astype(np.uint8)
out_arr[:, :, 3] = alpha.astype(np.uint8)

out_img = Image.fromarray(out_arr, mode='RGBA')

bbox = out_img.getbbox()
if bbox:
    # Add 2px safety margin
    bbox = (max(0, bbox[0]-2), max(0, bbox[1]-2), min(out_img.width, bbox[2]+2), min(out_img.height, bbox[3]+2))
    out_img = out_img.crop(bbox)

# Upscale 3x with Lanczos for smooth high-DPI rendering
out_img = out_img.resize((out_img.width * 3, out_img.height * 3), Image.Resampling.LANCZOS)
out_img.save(dest_path, 'PNG')
print(f"Successfully generated high-res transparent gold rings: {out_img.size}")
