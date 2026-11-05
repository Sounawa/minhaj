import sys
from PIL import Image
# usage: crop.py src out top bottom [dpi_scale]  (top/bottom = fraction of height)
src, out = sys.argv[1], sys.argv[2]
top, bot = float(sys.argv[3]), float(sys.argv[4])
im = Image.open(src)
w, h = im.size
im.crop((0, int(h*top), w, int(h*bot))).save(out)
print(out, im.size, "->", (w, int(h*(bot-top))))
