# Homework 5

## Problem 1: Fraction

**Place your solution in `problem1/fraction.py`.**

Write a class named `Fraction` that represents a rational number (a number that can be expressed as a quotient of two integers).

It is required to have the following methods:

- A constructor that takes two integers, `numerator` and `denominator`.
  - If the denominator is ever set to 0, a `ZeroDivisionError` exception should be raised.
  - The fraction should be stored in the lowest possible terms, that is to say, if you are passed 28/20 it should be normalized to 7/5. (You may use the `math.gcd` function to help with this.)
- `numerator` and `denominator` should be accessible as read-only properties.  That is to say, our `Fraction`` is immutable once created.
- Implement the basic binary operators `+, -, *, and /`. It should be possible to use any of these with two `Fraction`s or a `Fraction` and an `int`.  Note that you may need to also implement the reversed operators for this to fully work.
- The `__neg__` method should work to negate the `Fraction` instance.
- The `__eq__` method should be implemented to allow direct comparisons between two fractions.  (**Note**: Consider implementing this early; until you do, other tests may not pass!)
- The `__repr__` method should return `Fraction(numerator, denominator)` (where the names are replaced with their respective values).

Complete tests are provided in `problem1/test_fraction.py`, which you can run via `pytest problem1`.

## Problem 2: CSG
In this problem, you will need to exercise your knowledge of operator overloading in Python to build an application that produces images of geometric objects using a technique called constructive solid geometry (CSG).

More information on CSG: https://en.wikipedia.org/wiki/Constructive_solid_geometry

CSG allows one to model arbitrary geometric objects by representing them as boolean operators applied to simple "primitives" representing basic geometric shapes.

Objects are represented as binary trees where the leaves are primitives and the nodes are operators (intersection, union, difference).

![](csg.png)

You will build an application that draws 2D CSG objects.

You will need to build two classes representing primitives: `Circle` and `Rectangle`. 
Additionally, you will write three classes representing operators: `Intersection`, `Union`, and `Difference`.

You will need to define an abstract base class `Drawable` that the primitives' subclass inherits from, and provides both an interface (set of abstract methods that the subclass must implement) and abstract methods, such as a `draw()` method that draws the shape.

To visualize the complex shapes represented by CSG binary trees, we will use the `Pillow` library which allows image manipulation on a pixel-by-pixel basis.

The classes representing primitives are all required to use `__contains__` to support the `in` operator to check whether a given tuple `(x, y)` is within the corresponding shape.


Detailed specifications for your classes are below:

### Drawable

- `Drawable` should be an abstract base class.
- It should have an abstract `__contains__(self, point)` method.
- The `__and__(self, other)` method which overloads the `&` operator should return an instance of `Intersection` representing the intersection of the two operands.
- The `__or__(self, other)` method which overloads the `|` operator should return an instance of `Union` representing the union of the two operands.
- The `__sub__(self, other)` method which overloads the `-` operator should return an instance of `Difference`, representing the difference between two operands.
- The `draw(self, img)` method accepts an instance of `PIL.Image` and draws the shape represented by `self`.
  - A simple method to draw the shape is to then iterate over all pixels in a grid, checking whether each point is `in` the shape, and if it is, color the pixel.

`PIL.Image`

Your draw method receives an instance of `PIL.Image`.

You will want to use the following properties/methods to draw on it:
  - The `img.width` and `img.height` properties.
  - `img.putpixel(point, 0)` where `point` is a `(x, y)` tuple will fill a single point. Leave the second parameter as zero, to draw in black.

One thing to note is that in computer graphics, the coordinate system starts at the top left corner and extends toward the bottom right.

So `img.putpixel((0, 0), 0)` draws a single point in the upper left corner,
and `img.putpixel((img.width-1, img.height-1), 0)` draws a single point in the bottom right corner.

### Circle

- `Circle(x, y, radius)` should construct a circle centered at `x, y` with the given radius, storing the values in instance attributes.
- It must override the abstract `__contains__(self, point)` method, returning `True` if the point is within the circle.


### Rectangle

- `Rectangle(x0, y0, x1, y1)` should construct a rectangle, storing the values in instance attributes.
  - (x0, y0) represents the upper left point
  - (x1, y1) represents the lower right point
- It must override the abstract `__contains__(self, point)` method, returning `True` if the point is within the rectangle.

### Operator Classes

- Each of the operator classes `Intersection`, `Union`, and `Difference` should have a constructor that accepts two arguments: `shape1` and `shape2` and stores them as instance variables.
- `Intersection`'s `__contains__(self, point)` method returns `True` iff the point is in both shapes specified in the initializer.
- `Union`'s `__contains__(self, point)` method returns `True` iff the point is in either shape specified in the initializer.
- `Difference`'s `__contains__(self, point)` method returns `True` iff the point is in `shape1` but not `shape2`.

**Don't overthink these, all three are relatively similar and simple.**

### Smiley Face

Once you're done building all of the classes, update the code to draw a smiley face within `__main__`.

You can draw it however you wish so long as it has two eyes and a mouth.

### Notes

#### Running Your Code

You are already set up with `poetry` from prior homework, you can run `poetry install` in the `homework5` directory to install the required 'Pillow' library.  (If you are getting errors on `import PIL` try this first!)

You can then run your application via `poetry run python problem2/csg.py`.

You will need to run tests via `poetry run pytest problem2`.  (Note: This is different from prior homework!)

#### Inheritance

Part of your grade for this assignment is for you to determine which classes should inherit from others.  Course staff will not help with questions specifically about this portion.  You need to determine whether a class should or shouldn't inherit.

#### Testing

When you run the tests for this portion, your output will be compared to the files in `problem2/expected`.

For failing tests, you will see error output like:

```AssertionError: Output did not match, difference saved to error-union.png and diff-union.png```

The 'union.png' portion of the filename indicates which test was running, you can look in `problem2/expected/union.png` (for example) to see the expected output.

The file that starts with `error-` is the output that your code generated.

The file that starts with `diff-` is a special diff file to help you debug your output.

In the `error-` images, pixels will be colored according to if they matched the expected output:
- Green pixels are pixels that matched the expected output.
- Red pixels are pixels that should have been black but were white.
- Blue pixels are pixels that should have been white but were black.
