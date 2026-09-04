from PIL import Image, ImageDraw
import numpy as np
import random
import math

# -----------------------------
# SETTINGS
# -----------------------------
W, H = 1200, 1800
random.seed(42)

img = Image.new("RGB", (W, H), (8, 12, 18))
draw = ImageDraw.Draw(img)

cx = W // 2

# -----------------------------
# FEATHER SHAFT
# -----------------------------
shaft_top = 220
shaft_bottom = 1650

# Curved shaft
points = []

for i in range(300):
    y = shaft_top + (shaft_bottom - shaft_top) * i / 299
    x = cx + 45 * math.sin((y - shaft_top) / 900)
    points.append((x, y))

draw.line(points, fill=(170, 125, 65), width=12)
draw.line(points, fill=(230, 190, 100), width=4)

# -----------------------------
# FEATHER BARBS
# -----------------------------
def shaft_x(y):
    return cx + 45 * math.sin((y - shaft_top) / 900)


for y in np.linspace(300, 1450, 850):

    x0 = shaft_x(y)

    # Feather gets wider near the middle
    relative = (y - 300) / 1150
    width = 250 * math.sin(math.pi * relative)

    if width < 5:
        continue

    # Left and right fibers
    for side in [-1, 1]:

        length = width * random.uniform(.75, 1.15)

        angle = random.uniform(-0.15, 0.15)

        x1 = x0 + side * length
        y1 = y - length * .55 + random.uniform(-15, 15)

        # Curved fiber
        pts = []

        for t in np.linspace(0, 1, 15):

            xx = x0 + (x1 - x0) * t
            yy = y + (y1 - y) * t

            curve = math.sin(t * math.pi) * 35 * side

            xx += curve

            pts.append((xx, yy))

        # Iridescent colors
        colors = [
            (15, 95, 75),
            (20, 130, 105),
            (15, 80, 150),
            (30, 150, 120),
            (10, 65, 110),
            (55, 160, 125)
        ]

        color = random.choice(colors)

        draw.line(
            pts,
            fill=color,
            width=random.choice([1, 1, 1, 2])
        )

# -----------------------------
# PEACOCK EYE
# -----------------------------
eye_x = cx
eye_y = 520

def ellipse(center, radius, color):
    x, y = center
    draw.ellipse(
        (x-radius, y-radius,
         x+radius, y+radius),
        fill=color
    )

# Outer green halo
ellipse((eye_x, eye_y), 240, (8, 70, 55))

# Blue ring
ellipse((eye_x, eye_y), 190, (15, 80, 150))

# Turquoise ring
ellipse((eye_x, eye_y), 145, (15, 160, 150))

# Gold ring
ellipse((eye_x, eye_y), 105, (210, 170, 55))

# Dark blue center
ellipse((eye_x, eye_y), 78, (5, 35, 80))

# Green inner shape
ellipse((eye_x, eye_y + 15), 55, (10, 110, 75))

# Black center
ellipse((eye_x, eye_y + 20), 35, (2, 12, 25))

# -----------------------------
# EYE HIGHLIGHTS
# -----------------------------
for i in range(150):

    angle = random.uniform(0, math.pi * 2)
    radius = random.uniform(90, 220)

    x = eye_x + math.cos(angle) * radius
    y = eye_y + math.sin(angle) * radius

    r = random.choice([1, 1, 2, 3])

    color = random.choice([
        (40, 180, 150),
        (30, 120, 190),
        (100, 200, 150),
        (220, 190, 70)
    ])

    draw.ellipse(
        (x-r, y-r, x+r, y+r),
        fill=color
    )

# -----------------------------
# FINE FEATHER HAIRS
# -----------------------------
for i in range(12000):

    y = random.uniform(280, 1450)

    x0 = shaft_x(y)

    rel = (y - 280) / 1170

    max_width = 260 * math.sin(math.pi * rel)

    if max_width <= 0:
        continue

    side = random.choice([-1, 1])

    length = random.uniform(30, max_width)

    x1 = x0 + side * length
    y1 = y - length * random.uniform(.25, .65)

    color = random.choice([
        (8, 75, 65),
        (10, 110, 90),
        (15, 130, 120),
        (15, 75, 130),
        (30, 150, 130),
        (50, 160, 120)
    ])

    draw.line(
        [(x0, y), (x1, y1)],
        fill=color,
        width=1
    )

# -----------------------------
# SHINE
# -----------------------------
shine = Image.new("RGBA", (W, H), (0, 0, 0, 0))
sd = ImageDraw.Draw(shine)

for i in range(300):

    x = random.randint(cx - 250, cx + 250)
    y = random.randint(250, 1450)

    sd.ellipse(
        (x, y, x+random.randint(1, 4), y+random.randint(1, 4)),
        fill=(100, 230, 210, random.randint(30, 120))
    )

img = Image.alpha_composite(
    img.convert("RGBA"),
    shine
)

# -----------------------------
# SAVE
# -----------------------------
img.save("ultra_realistic_peacock_feather.png")

print("Saved: ultra_realistic_peacock_feather.png")
