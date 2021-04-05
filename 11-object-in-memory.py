### objects in memory
## in Python everything is an object - an instance of the object class

### LISTS
## These are some built-in list methods in Python:
# .extend()
# .append()
# .insert()
# .count()
# .index()
# .sort()
# .pop()
# .remove()

### using id()
a = [1, 2, 3, 4, 5]
b = [1, 2, 3, 4, 5]
id(a)
id(b)

### is operator
# checks if two objects are referenced by the same memory address (object in memory)
# is ==> same object
# == ==> same value
a is b
a == b
c = a

c is a
c == a

### == operator
# Objects created from user-defined classes have to meet two conditions for the expression obj1 == obj2 to evaluate to True.
# They have to refer to the same object (x is y has to evaluate to True)
# The expression hash(x) == hash(y) has to evaluate to True
# The hash() function maps the object to a unique integer. For more information on the hash() built-in function


class Dog:
    def __init__(self, age):
        self.age = age


a = Dog(5)
b = Dog(5)
a is b
hash(a)
hash(b)
a == b  # False
a == a  # True
b == b  # True
b == a  # False


### is - unexpected results
x = 5
z = 5
x is z  # True for small integers [-5, 256]

e = "H"
f = "H"
e is f
g = "Hello, world!"
len(g)
g[
    1
] = "a"  # Strings in Python are immutable so same strings are treated as the same objects in memory
id(e)
id(f)

## rules of string intering - MEMORY OPTIMIZATION OF THE PYTHON LANGUAGE
# all length 0 or 1 strings are interned
# strings that are composed only of ASCII letters (a-z, A-Z), digits (0-9) or underscores are interned

### Different Behavior: Shell vs. Script
# The environment in which you run the code affects how string interning works.
# The behavior can be different when you are using the interactive console or when you are running a Python script, depending on how the code is optimized behind the scenes when the program runs.
# This is because different environments have different optimization levels.
# The process can also vary between different versions of Python.
# Example:
# If you run this code in the Python Shell (console), you will see False:

a = "Hello, World!"
b = "Hello, World!"
a is b  # False

# But if you run it from a Python script, you will see True as the result for a is b.


### working with objects
# objects are passed by reference   
a = [5, 6, 2]

# Function that takes a list object as argument
def f(x):
    print(id(x))
    return x


id(a)
f(a)