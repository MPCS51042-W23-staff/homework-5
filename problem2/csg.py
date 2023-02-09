import math
from abc import ABC, abstractmethod
from PIL import Image


def main():
    # You may modify this method as you see fit.
    # Remember to draw a happy face before submitting!

    # create a blank white image
    width = 500
    height = 500
    img = Image.new("RGB", (width, height), "white")

    # build a drawable here
    to_draw = Circle(200, 200, 100)

    # an example of `Difference`
    # to_draw = Circle(200, 200, 100) - Rectangle(150, 150, 250, 250)

    # draw drawables to img and then save to output.png
    to_draw.draw(img)
    img.save("output.png")


if __name__ == "__main__":
    main()
