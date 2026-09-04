"""
Animated, hand-built realistic peacock feather.
Single Python file.
Uses ONLY Python Turtle + standard library.

No PNG/JPG/SVG or external image files.
"""

import math
import random
import time
import turtle


# ============================================================
# SETTINGS
# ============================================================

random.seed(23)

WIDTH = 1000
HEIGHT = 760

BG = "#020907"

# Animation controls
# Increase DRAW_DELAY for slower animation.
# Decrease it for faster animation.
DRAW_DELAY = 0.012

FRAME_EVERY = 28

operation_count = 0


screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.title("Peacock Feather — Hand Drawn")
screen.bgcolor(BG)

screen.tracer(0, 0)

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.penup()

def rgba_mix(first, second, amount):
    """
    Mix two hexadecimal colors.
    Used to simulate subtle color transitions.
    """

    amount = max(0.0, min(1.0, amount))

    a = tuple(
        int(first[index:index + 2], 16)
        for index in (1, 3, 5)
    )

    b = tuple(
        int(second[index:index + 2], 16)
        for index in (1, 3, 5)
    )

    values = [
        round(a[i] + (b[i] - a[i]) * amount)
        for i in range(3)
    ]

    return "#" + "".join(
        f"{value:02x}"
        for value in values
    )

def pause_frame(force=False):
    """
    Refresh the Turtle screen only occasionally.

    The original version refreshed the screen thousands
    of times. This version batches drawing operations so
    the animation remains smooth but dramatically faster.
    """

    global operation_count

    operation_count += 1

    if force or operation_count % FRAME_EVERY == 0:
        screen.update()

        if DRAW_DELAY > 0:
            time.sleep(DRAW_DELAY)


def curve_points(start, end, bend=0.0, steps=6):
    """
    Create a gently curved quadratic line.
    """

    midpoint = (
        (start[0] + end[0]) / 2,
        (start[1] + end[1]) / 2
    )

    dx = end[0] - start[0]
    dy = end[1] - start[1]

    length = max(1.0, math.hypot(dx, dy))

    control = (
        midpoint[0] - dy / length * bend,
        midpoint[1] + dx / length * bend
    )

    points = []

    for index in range(steps + 1):

        t = index / steps

        x = (
            (1 - t) ** 2 * start[0]
            + 2 * (1 - t) * t * control[0]
            + t ** 2 * end[0]
        )

        y = (
            (1 - t) ** 2 * start[1]
            + 2 * (1 - t) * t * control[1]
            + t ** 2 * end[1]
        )

        points.append((x, y))

    return points

def stroke(points, color, width=1, animate=False):
    """
    Draw a line through points.

    Animation is intentionally batched.
    """

    pen.color(color)
    pen.width(width)

    pen.penup()
    pen.goto(points[0])
    pen.pendown()

    for point in points[1:]:
        pen.goto(point)

    pen.penup()

    if animate:
        pause_frame()


def draw_fiber(start, end, color, width=1, bend=0):
    """
    Draw one feather fiber.

    One complete fiber is treated as one animation unit.
    """

    points = curve_points(
        start,
        end,
        bend,
        steps=6
    )

    stroke(
        points,
        color,
        width,
        animate=False
    )

    pause_frame()

def shaft_point(t):
    """
    Main curved feather shaft.

    t = 0 -> bottom-left
    t = 1 -> upper-right
    """

    return (
        -370 + 735 * t,

        -292
        + 600 * t
        + 24 * math.sin(t * math.pi * 0.85)
    )


def draw_shaft():

    shaft = [
        shaft_point(index / 50)
        for index in range(51)
    ]

    stroke(
        shaft,
        "#28150e",
        9,
        animate=True
    )

 
    stroke(
        shaft,
        "#6b3b21",
        6,
        animate=True
    )

   
    stroke(
        shaft,
        "#b87538",
        3,
        animate=True
    )


    stroke(
        shaft,
        "#e0a65a",
        1,
        animate=True
    )

    stroke(
        [
            shaft_point(index / 60)
            for index in range(61)
        ],
        "#382016",
        1,
        animate=True
    )

def barb_end(base, side, length, variation):

    direction = 1 if side > 0 else -1

    curve_factor = (
        0.62
        + 0.06 * math.sin(variation)
        + random.uniform(-0.035, 0.035)
    )

    vertical_factor = (
        0.72
        + 0.05 * math.cos(variation)
        + random.uniform(-0.04, 0.04)
    )

    x = base[0] + length * curve_factor

    y = (
        base[1]
        + direction * length * vertical_factor
    )

    return x, y


def draw_barb(base, side, length, color, detail=True):

    direction = 1 if side > 0 else -1

    endpoint = barb_end(
        base,
        side,
        length,
        base[0] * 0.03
    )

    bend = (
        direction * random.uniform(8, 34)
        + random.uniform(-9, 9)
    )

    draw_fiber(
        base,
        endpoint,
        color,
        random.choice((1, 1, 1, 2)),
        bend
    )

    if not detail:
        return

    fractions = (
        0.20,
        0.34,
        0.48,
        0.61,
        0.73,
        0.84
    )

    for fraction in fractions:

        origin = (
            base[0]
            + (endpoint[0] - base[0]) * fraction,

            base[1]
            + (endpoint[1] - base[1]) * fraction
        )

        remaining = (
            length
            * (
                0.13
                + 0.22 * (1 - fraction)
            )
        )

        secondary = (
            origin[0]
            + remaining
            * (
                0.40
                + random.random() * 0.22
            ),

            origin[1]
            + direction
            * remaining
            * (
                0.50
                + random.random() * 0.25
            )
        )

        fine = rgba_mix(
            color,
            "#03100c",
            random.uniform(0.08, 0.35)
        )

        draw_fiber(
            origin,
            secondary,
            fine,
            1,
            direction * random.uniform(3, 15)
        )

def draw_feather_body():

    palette = [
        "#0d3525",
        "#123e2b",
        "#176248",
        "#21815c",
        "#2d9569",
        "#3ba478",
        "#57994f",
        "#6e9d4d",
        "#2b6651",
        "#174a55",
        "#286d5e",
    ]
    for index in range(1050):

        t = (
            0.035
            + (index % 260) / 270 * 0.925
        )

        t += random.uniform(
            -0.012,
            0.012
        )

        t = max(
            0.02,
            min(0.985, t)
        )

    
        side = (
            1
            if index % 2
            else -1
        )

        if t > 0.72 and side < 0:
            if random.random() < 0.70:
                side = 1

        base = shaft_point(t)

        taper = math.sin(
            math.pi * min(1.0, t)
        )

        max_length = (
            40
            + 210
            * taper
            * (
                0.78
                + random.random() * 0.32
            )
        )

        # Taper toward tip
        if t > 0.76:
            max_length *= (
                (1.02 - t) * 4.2
            )

        length = max(
            22,
            max_length
        )

        color = random.choice(
            palette
        )

        # Occasional golden fibers
        if index % 13 == 0:

            color = rgba_mix(
                color,
                "#b6b44a",
                random.uniform(
                    0.12,
                    0.32
                )
            )

       
        if index % 17 == 0:

            color = rgba_mix(
                color,
                "#061813",
                random.uniform(
                    0.20,
                    0.45
                )
            )

        draw_barb(
            base,
            side,
            length,
            color,
            detail=(index % 3 != 0)
        )

def irregular_ring(
    center,
    radius_x,
    radius_y,
    color,
    count=60,
    width=2
):

    points = []

    for index in range(count + 1):

        angle = (
            math.tau
            * index
            / count
        )

        wobble = (
            1
            + random.uniform(
                -0.035,
                0.035
            )
        )

        x = (
            center[0]
            + math.cos(angle)
            * radius_x
            * wobble
        )

        y = (
            center[1]
            + math.sin(angle)
            * radius_y
            * wobble
        )

        points.append(
            (x, y)
        )

    stroke(
        points,
        color,
        width,
        animate=True
    )


def draw_eye():

    center = (
        238,
        257
    )


    for layer in range(18):

        rx = 146 - layer * 5.8
        ry = 184 - layer * 7.1

        color = rgba_mix(
            "#152f1a",
            "#a06b2e",
            layer / 20
        )

        irregular_ring(
            center,
            rx,
            ry,
            color,
            60,
            2
        )

        if layer % 2 == 0:
            pause_frame()


    for layer in range(14):

        rx = 112 - layer * 4.0
        ry = 143 - layer * 5.0

        color = rgba_mix(
            "#476728",
            "#1e9b65",
            layer / 15
        )

        irregular_ring(
            center,
            rx,
            ry,
            color,
            55,
            2
        )

        if layer % 2 == 0:
            pause_frame()

    for layer in range(12):

        rx = 78 - layer * 3.0
        ry = 104 - layer * 4.0

        color = rgba_mix(
            "#19b58c",
            "#27d0c6",
            layer / 13
        )

        irregular_ring(
            center,
            rx,
            ry,
            color,
            52,
            2
        )

        if layer % 2 == 0:
            pause_frame()


    for layer in range(10):

        rx = 52 - layer * 2.5
        ry = 72 - layer * 3.1

        color = rgba_mix(
            "#1263a6",
            "#12367e",
            layer / 11
        )

        irregular_ring(
            center,
            rx,
            ry,
            color,
            48,
            2
        )

        if layer % 2 == 0:
            pause_frame()

    for layer in range(8):

        rx = 31 - layer * 2.1
        ry = 46 - layer * 2.7

        color = rgba_mix(
            "#321f6b",
            "#070c2a",
            layer / 9
        )

        irregular_ring(
            center,
            rx,
            ry,
            color,
            42,
            2
        )

        if layer % 2 == 0:
            pause_frame()
    draw_eye_fibers(
        center
    )

def draw_eye_fibers(center):

    eye_colors = [
        "#2ad0ae",
        "#53b85a",
        "#328fc4",
        "#4a4ca0",
        "#c99745",
        "#163f75",
        "#4ebc91",
        "#78a74a",
    ]

    for index in range(300):

        angle = random.uniform(
            0,
            math.tau
        )

        inner = random.uniform(
            45,
            83
        )

        outer = (
            inner
            + random.uniform(
                20,
                78
            )
        )

        start = (
            center[0]
            + math.cos(angle)
            * inner,

            center[1]
            + math.sin(angle)
            * inner
            * 1.28
        )

        angle2 = (
            angle
            + random.uniform(
                -0.08,
                0.08
            )
        )

        end = (
            center[0]
            + math.cos(angle2)
            * outer,

            center[1]
            + math.sin(angle2)
            * outer
            * 1.28
        )

        draw_fiber(
            start,
            end,
            random.choice(
                eye_colors
            ),
            1,
            random.uniform(
                -15,
                15
            )
        )


def draw_highlights():

    for index in range(95):

        t = random.uniform(
            0.08,
            0.92
        )

        side = random.choice(
            (-1, 1)
        )

        base = shaft_point(t)

        length = (
            random.uniform(
                25,
                155
            )
            * math.sin(
                math.pi * t
            )
        )

        end = barb_end(
            base,
            side,
            length,
            index
        )

        color = random.choice(
            (
                "#9bd174",
                "#78c7aa",
                "#d2c467",
                "#48b8b0",
                "#b6d87c",
                "#6dbb91"
            )
        )

        draw_fiber(
            base,
            end,
            color,
            1,
            side * random.uniform(
                8,
                24
            )
        )


    for index in range(55):

        x = random.uniform(
            -20,
            360
        )

        y = random.uniform(
            -10,
            415
        )

        points = [
            (x, y),
            (
                x + random.uniform(
                    2,
                    7
                ),
                y + random.uniform(
                    1,
                    6
                )
            )
        ]

        stroke(
            points,
            random.choice(
                (
                    "#c9dc8d",
                    "#6dd0ad",
                    "#d6b75d",
                    "#8ecf91"
                )
            ),
            1,
            animate=True
        )



def draw_background():

    colors = [
        "#03100c",
        "#04130f",
        "#051610",
        "#061812"
    ]

    for index in range(22):

        y = random.uniform(
            -HEIGHT / 2,
            HEIGHT / 2
        )

        start = (
            -WIDTH / 2,
            y
        )

        end = (
            WIDTH / 2,
            y + random.uniform(
                -35,
                35
            )
        )

        points = curve_points(
            start,
            end,
            random.uniform(
                -25,
                25
            ),
            10
        )

       
        stroke(
            points,
            random.choice(colors),
            random.choice((1, 1, 2)),
            animate=False
        )

    screen.update()

def final_details():

    for index in range(35):

        t = random.uniform(
            0.02,
            0.30
        )

        base = shaft_point(t)

        side = random.choice(
            (-1, 1)
        )

        length = random.uniform(
            35,
            130
        )

        end = barb_end(
            base,
            side,
            length,
            index
        )

        draw_fiber(
            base,
            end,
            random.choice(
                (
                    "#071b14",
                    "#092219",
                    "#123326",
                    "#183b2d"
                )
            ),
            1,
            side * random.uniform(
                5,
                20
            )
        )


def main():

    draw_background()
    draw_shaft()
    draw_feather_body()
    draw_eye()
    draw_highlights()
    final_details()

    screen.update()
    screen.mainloop()

if __name__ == "__main__":
    main()
