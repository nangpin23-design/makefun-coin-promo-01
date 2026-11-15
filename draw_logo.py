"""Draw the BountyBot logo: one bold robot head on a plain bright background.

BountyBot is a little robot that hunts paid bounties on make.fun: it reads the
board, builds an entry, and climbs the leaderboard. The logo is a single bold
subject (the robot's head and shoulders) with a strong dark outline and high
contrast, so it reads at pump.fun thumbnail size. No text is baked into the
logo art itself; the ticker is shown by pump.fun beside it.
"""
import math
from PIL import Image, ImageDraw, ImageFont

W = 1024
NAVY = (20, 33, 61, 255)      # strong outline / body
TEAL = (18, 181, 165, 255)    # robot head
YELLOW = (255, 199, 0, 255)   # plain bright background
GOLD = (255, 183, 3, 255)     # star / medal
WHITE = (255, 255, 255, 255)
PINK = (255, 150, 170, 255)   # cheek blush
ORANGE = (255, 107, 53, 255)  # ear bolts

img = Image.new("RGBA", (W, W), YELLOW)
d = ImageDraw.Draw(img)


def star(cx, cy, r_outer, r_inner, fill, outline=None, width=1):
    pts = []
    for i in range(10):
        r = r_outer if i % 2 == 0 else r_inner
        a = math.pi / 2 + i * math.pi / 5  # point up
        pts.append((cx + r * math.cos(a - math.pi / 2 + math.pi / 2 * 0) * 0 + r * math.cos(math.pi / 2 + i * math.pi / 5 - math.pi / 2),
                    cy - r * math.sin(math.pi / 2 + i * math.pi / 5)))
    # simpler correct star: angle starts at -90deg, step 36deg
    pts = []
    for i in range(10):
        r = r_outer if i % 2 == 0 else r_inner
        ang = -math.pi / 2 + i * math.pi / 5
        pts.append((cx + r * math.cos(ang), cy + r * math.sin(ang)))
    if outline:
        d.polygon(pts, fill=fill, outline=outline)
        d.line(pts + [pts[0]], fill=outline, width=width, joint="curve")
    else:
        d.polygon(pts, fill=fill)


# Antenna stem + gold star on top
d.line([(512, 228), (512, 128)], fill=NAVY, width=18)
star(512, 96, 58, 24, GOLD, outline=NAVY, width=8)

# Ear bolts
for cx in (222, 802):
    d.ellipse([cx - 30, 400, cx + 30, 460], fill=ORANGE, outline=NAVY, width=10)

# Robot head: rounded square, teal with thick navy outline
d.rounded_rectangle([232, 220, 792, 648], radius=92, fill=TEAL, outline=NAVY, width=18)

# Eyes: big white circles, navy pupils looking up (toward the leaderboard)
for cx in (368, 656):
    d.ellipse([cx - 64, 330, cx + 64, 458], fill=WHITE, outline=NAVY, width=10)
    d.ellipse([cx - 26, 352, cx + 26, 404], fill=NAVY)
    d.ellipse([cx + 6, 360, cx + 18, 372], fill=WHITE)  # glint

# Cheek blush
for cx in (318, 706):
    d.ellipse([cx - 24, 492, cx + 24, 532], fill=PINK)

# Smile: a wide open grin
d.arc([408, 452, 616, 620], start=15, end=165, fill=NAVY, width=16)

# Shoulders / body: navy, with a gold star medal on the chest
d.rounded_rectangle([296, 648, 728, 924], radius=64, fill=NAVY)
star(512, 762, 66, 27, GOLD, outline=WHITE, width=6)

# Ticker on the chest, bold white
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 72)
text = "BNTY"
bbox = d.textbbox((0, 0), text, font=font)
tw = bbox[2] - bbox[0]
d.text((512 - tw / 2, 838), text, font=font, fill=WHITE)

img.convert("RGB").save("/home/hatch/workspace/makefun/makefun-coin-promo-01-clean/logo.png", optimize=True)
print("saved logo.png")
