import turtle
import math
import random

# =========================================================
# PEACOCK FEATHER — CENTERED + SMALLER + DETAILED
# =========================================================

screen = turtle.Screen()
screen.setup(800, 800)
screen.bgcolor("#071426")
screen.title("Krishna's Peacock Feather")

# About 5x faster than normal Turtle drawing
screen.tracer(0, 0)

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

random.seed(10)


# =========================================================
# BASIC FUNCTIONS
# =========================================================

def ellipse(x, y, rx, ry, color):
    t.penup()
    t.goto(x + rx, y)
    t.pendown()

    t.color(color)
    t.begin_fill()

    for i in range(50):
        angle = 2 * math.pi * i / 50

        t.goto(
            x + rx * math.cos(angle),
            y + ry * math.sin(angle)
        )

    t.end_fill()


def line(points, color, width=1):
    t.color(color)
    t.pensize(width)

    t.penup()
    t.goto(points[0])
    t.pendown()

    for p in points[1:]:
        t.goto(p)


# =========================================================
# FEATHER POSITION
# =========================================================

# Everything is centered around this point
CENTER_X = 0
CENTER_Y = 20


# =========================================================
# FEATHER STEM
# =========================================================

def stem_x(y):

    # Gentle curve
    return CENTER_X + 0.00025 * (y + 260) ** 2 - 35


stem = []

for i in range(130):

    y = -280 + i * 4

    stem.append(
        (stem_x(y), y)
    )

# Main stem
line(stem, "#795021", 8)

# Golden highlight
line(stem, "#D4A548", 2)


# =========================================================
# FEATHER BARBS
# =========================================================

# Moderate number of strands
for i in range(260):

    y = -120 + i * 2.8

    if y > 610:
        break

    x0 = stem_x(y)

    progress = (y + 120) / 730

    # Smaller feather width
    width = 205 * math.sin(progress * math.pi)

    if width < 5:
        continue

    for side in [-1, 1]:

        length = width * random.uniform(
            0.75,
            1.0
        )

        x1 = x0 + side * length

        y1 = y + length * 0.42

        curve = side * random.uniform(
            8,
            22
        )

        points = [
            (x0, y),

            (
                x0 + (x1 - x0) * .5 + curve,
                y + (y1 - y) * .5
            ),

            (x1, y1)
        ]

        color = random.choice([
            "#087965",
            "#07957B",
            "#126A9C",
            "#1686B4",
            "#159D81",
            "#0B5478"
        ])

        line(
            points,
            color,
            1
        )


# =========================================================
# PEACOCK EYE
# =========================================================

eye_x = CENTER_X - 10
eye_y = 390


# Outer green
ellipse(
    eye_x,
    eye_y,
    135,
    175,
    "#07553F"
)

# Bright green
ellipse(
    eye_x,
    eye_y,
    115,
    150,
    "#078260"
)

# Dark blue
ellipse(
    eye_x,
    eye_y + 5,
    95,
    125,
    "#075399"
)

# Blue
ellipse(
    eye_x,
    eye_y + 8,
    78,
    105,
    "#1189C2"
)

# Turquoise
ellipse(
    eye_x,
    eye_y + 8,
    59,
    83,
    "#10B398"
)

# Gold
ellipse(
    eye_x,
    eye_y + 8,
    43,
    62,
    "#D8AA2F"
)

# Dark blue
ellipse(
    eye_x,
    eye_y + 12,
    34,
    50,
    "#06396D"
)

# Green
ellipse(
    eye_x,
    eye_y + 16,
    24,
    38,
    "#08734D"
)

# Black pupil
ellipse(
    eye_x,
    eye_y + 19,
    13,
    27,
    "#01050A"
)


# =========================================================
# EYE RAYS
# =========================================================

for i in range(100):

    angle = random.uniform(
        0,
        math.pi * 2
    )

    r1 = random.uniform(
        80,
        110
    )

    r2 = random.uniform(
        120,
        155
    )

    x1 = eye_x + math.cos(angle) * r1
    y1 = eye_y + math.sin(angle) * r1

    x2 = eye_x + math.cos(angle) * r2
    y2 = eye_y + math.sin(angle) * r2

    line(
        [(x1, y1), (x2, y2)],
        random.choice([
            "#18B99A",
            "#168DC0",
            "#3BCBA0",
            "#D2B33A"
        ]),
        1
    )


# =========================================================
# SMALL FEATHER DETAILS
# =========================================================

for i in range(180):

    angle = random.uniform(
        0,
        math.pi * 2
    )

    radius = random.uniform(
        70,
        180
    )

    x = eye_x + math.cos(angle) * radius
    y = eye_y + math.sin(angle) * radius

    t.penup()
    t.goto(x, y)

    t.dot(
        random.choice([1, 2, 2]),
        random.choice([
            "#28BFA1",
            "#319FC4",
            "#D5BD55"
        ])
    )


# =========================================================
# EYE HIGHLIGHT
# =========================================================

t.penup()
t.goto(
    eye_x - 10,
    eye_y + 40
)
t.dot(10, "#C8FFF4")

t.goto(
    eye_x - 18,
    eye_y + 55
)
t.dot(4, "white")


# =========================================================
# GOLDEN CLASP
# =========================================================

for i in range(7):

    x = -70 + i * 12
    y = -265 + math.sin(i) * 4

    t.penup()
    t.goto(x, y)
    t.dot(9, "#FFD34E")


# =========================================================
# FINISH
# =========================================================

screen.update()
turtle.done()
