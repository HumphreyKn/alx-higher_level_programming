# Python- Import and Modules
## Learning Objectives

### Importing Functions from Another File:
In Python, you can organize your code into separate files or modules to make it more manageable. To use functions defined in another file/module, you need to import them using the import statement.

```
# Import a function from another file
from mymodule import my_function

# Now you can use my_function
result = my_function()
```

### Using Imported Functions:
Once you've imported a function from another module, you can use it just like any other function in your script. You simply call the imported function by its name.

### Creating a Module:
In Python, a module is a file containing Python definitions, functions, and statements. To create a module, you need to save your code in a .py file. For example, you can create a module named mymodule.py:

```
# mymodule.py (name of the file)
def my_function():
    return "Hello from my_function in mymodule!"
```

### Using the `dir()` Built-in Function:
The `dir()` function is used to get a list of all names (variables, functions, classes, etc.) defined in a module or the current scope. It's a useful tool for exploring the contents of a module.

Example:
```python
import mymodule
print(dir(mymodule))
```

### Preventing Code Execution When Imported:
Sometimes, you want to execute code only when the script is run directly (not when it's imported as a module). You can achieve this by using the special variable `__name__`. When a Python script is run, the `__name__` variable is set to `"__main__"`; otherwise, it's set to the module's name. You can use this to conditionally execute code.

Example:
```python
# mymodule.py
def my_function():
    return "Hello from my_function in mymodule!"

if __name__ == "__main__":
    # This code will only execute when mymodule is run directly
    print("This code is only executed when mymodule is run directly.")
```

### Using Command Line Arguments:
Python allows you to access command line arguments using the `sys.argv` list provided by the `sys` module. The `sys.argv` list contains the command-line arguments passed to the script.

Example:
```python
# myscript.py
import sys

if len(sys.argv) > 1:
    arg1 = sys.argv[1]
    print(f"Command line argument 1 is: {arg1}")
else:
    print("No command line arguments provided.")
```
Running this script from the command line: `python myscript.py argument1` would print "Command line argument 1 is: argument1."

