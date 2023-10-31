# CPython implementation of small integers

## Question:
```python
a = 1
b = 1
```

Assuming we are using a CPython implementation of Python3 with default options/configuration:

    How many int objects are created by the execution of the first line of the script? (103-line1.txt)
    How many int objects are created by the execution of the second line of the script (103-line2.txt)

## Explanation
In CPython, the standard Python implementation, small integers in the range -5 to 256 are preallocated and cached for performance reasons. When you create integer variables within this range, they usually refer to the same preallocated object. This means that for small integers, such as 1, as in your example, the number of int objects created may be fewer than expected.

1. The first line `a = 1` creates one int object for the value 1. It doesn't create a new int object because Python uses an existing cached object for the integer 1 in this range.

2. The second line `b = 1` also does not create a new int object. It uses the same cached int object for the value 1. So, no new int objects are created by the second line either.

In summary, no new int objects are created by either of the two lines in your script because Python reuses the cached integer objects for small integers like 1.
