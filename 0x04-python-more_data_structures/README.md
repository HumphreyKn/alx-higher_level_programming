# Python Data Structures: Set, Dictionary 

## Sets in Python

### What are sets and how to use them
A set in Python is an unordered collection of unique elements. It is defined using curly braces `{}` or the `set()` constructor. Sets are commonly used when you want to store a collection of items where uniqueness is important.

#### Example:
```python
my_set = {1, 2, 3, 4}
```

### Common Set Methods and Usage
- `add(element)`: Adds an element to the set.
- `remove(element)`: Removes an element from the set.
- `union(other_set)`: Returns a new set containing elements from both sets.
- `intersection(other_set)`: Returns a new set containing common elements.
- `difference(other_set)`: Returns a new set with elements from the first set not in the second.

### When to use sets versus lists
Use sets when you need to store unique items and order doesn't matter. Lists, on the other hand, allow duplicate elements and maintain order.

### How to iterate over a set
You can iterate through a set using a for loop:

```python
my_set = {1, 2, 3}
for item in my_set:
    print(item)
```

## Dictionaries in Python

### What are dictionaries and how to use them
A dictionary is an unordered collection of key-value pairs. Keys are unique, and values can be of any data type. Dictionaries are created using curly braces `{}` or the `dict()` constructor.

#### Example:
```python
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
```

### When to use dictionaries versus lists or sets
Use dictionaries when you need to associate keys with values, making it easy to access and manipulate data by key. Lists are used for ordered collections, while sets are for storing unique values.

### What is a key in a dictionary
A key in a dictionary is a unique identifier associated with a value. Keys are used to access values in the dictionary.

### How to iterate over a dictionary
You can iterate over the keys, values, or key-value pairs in a dictionary using a for loop:

```python
my_dict = {'name': 'John', 'age': 30}
for key in my_dict:
    print(key, my_dict[key])

for value in my_dict.values():
    print(value)

for key, value in my_dict.items():
    print(key, value)
```

## Lambda Functions

### What is a lambda function
A lambda function is an anonymous, small, and inline function defined using the `lambda` keyword. It's used for simple operations and does not require a separate function definition.

#### Example:
```python
add = lambda x, y: x + y
result = add(2, 3)  # Result is 5
```

## Map, Reduce, and Filter Functions

These functions are built-in in Python and are often used in conjunction with lambda functions.

- `map(function, iterable)`: Applies a function to each element of an iterable and returns a map object.
- `reduce(function, iterable)`: Repeatedly applies a function to the elements of an iterable, reducing it to a single value.
- `filter(function, iterable)`: Filters elements of an iterable based on a given function, returning those for which the function returns `True`.

#### Example (using map and lambda):
```python
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))  # Result is [1, 4, 9, 16, 25]
```

These functions are powerful tools for working with data efficiently.
