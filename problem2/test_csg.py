import pytest
import math
import functools
from csg import Circle, Rectangle
from PIL import Image
from pathlib import Path

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
CORRECT_COLOR = (0, 255, 0)
EXPECTED_COLOR = (255, 0, 0)
EXTRA_COLOR = (0, 0, 255)
WIDTH = 500
HEIGHT = 500
relpath = Path(__file__).parent / "expected"


def programmatic():
    rings = [
        Circle(
            250 - 150 * math.sin(math.pi / 4 * n),
            250 - 150 * math.cos(math.pi / 4 * n),
            70,
        ) - 
        Circle(
            250 - 150 * math.sin(math.pi / 4 * n),
            250 - 150 * math.cos(math.pi / 4 * n),
            60,
        )
        for n in range(8)
    ]
    rings = functools.reduce(lambda a, b: a | b, rings)

    ccs = [
        Circle(250, 250, n) - Circle(250, 250, n-20)
        for n in range(20, 260, 40)
    ]
    ccs = functools.reduce(lambda a, b: a | b, ccs)
    return rings & ccs


TEST_CASES = {
    "circle.png": Circle(250, 250, 150),
    "rectangle.png": Rectangle(100, 100, 300, 400),
    "union.png": Circle(200, 200, 100) | Circle(250, 250, 75),
    "union-many.png": Circle(200, 200, 100)
    | Rectangle(100, 50, 300, 100)
    | Rectangle(100, 300, 300, 350)
    | Rectangle(50, 200, 350, 250),
    "intersection.png": Circle(100, 100, 100) & Rectangle(0, 0, 100, 300),
    "intersection-many.png": Circle(200, 200, 100)
    & Rectangle(0, 200, 1000, 220)
    & Circle(200, 200, 50),
    "difference.png": Circle(200, 200, 100) - Circle(200, 200, 50),
    "difference-many.png": Rectangle(0, 0, 500, 500)
    - (Circle(200, 200, 100) - Circle(200, 200, 50))
    - (Rectangle(300, 300, 450, 450) - Rectangle(350, 350, 400, 400)),
    "art1.png": (Circle(250, 250, 250) - Circle(250, 250, 200))
    & (
        Rectangle(0, 0, 500, 50)
        | Rectangle(0, 100, 500, 140)
        | Rectangle(0, 180, 500, 210)
        | Rectangle(0, 240, 500, 260)
        | Rectangle(0, 280, 500, 290)
        | Rectangle(0, 300, 500, 305)
    ),
    "art2.png": programmatic(),
}


def imagediff(filename, actual):
    expected = Image.open(relpath / filename)
    assert expected.width == actual.width, "Widths Differ"
    assert expected.height == actual.height, "Heights Differ"

    output = Image.new("RGB", (expected.width, expected.height), "white")
    errors = 0

    for x in range(expected.width):
        for y in range(expected.height):
            pt = (x, y)
            if expected.getpixel(pt) == WHITE and actual.getpixel(pt) == BLACK:
                output.putpixel(pt, EXTRA_COLOR)
                errors += 1
            elif expected.getpixel(pt) == BLACK and actual.getpixel(pt) == WHITE:
                output.putpixel(pt, EXPECTED_COLOR)
                errors += 1
            else:
                output.putpixel(pt, CORRECT_COLOR)

    if errors:
        actual.save("error-" + filename)
        output.save("diff-" + filename)
        raise AssertionError(
            f"Output did not match, difference saved to error-{filename} and diff-{filename}"
        )


@pytest.mark.parametrize("filename,drawable", TEST_CASES.items())
def test_drawable(filename, drawable):
    actual = Image.new("RGB", (WIDTH, HEIGHT), "white")
    drawable.draw(actual)
    imagediff(filename, actual)


if __name__ == "__main__":
    # if invoked as main, will regenerate all test images
    for filename, drawable in TEST_CASES.items():
        expected = Image.new("RGB", (WIDTH, HEIGHT), "white")
        drawable.draw(expected)
        expected.save(relpath / filename)
