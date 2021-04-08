# special = magick = dunder methods
# The main functional difference between special methods and common methods is that special methods run when we use a special syntax
# (such as arithmetic operations or subscripting and slicing) instead of direct method calls
# In general, the names of special methods have double leading and trailing underscores


5 + 6
# is the same as
(5).__add__(6)

## examples of special methods
# __add__()
# __str__()
# __repr__()
# __len___()
# __getitem__()
# __init__()


### __str__() ####
# is triggered when you try to print the instance of the class
# Used to provide an informal representation of the object meant for the final users.
# Favores readability over details or precision.
# Called by the str() , format(), and print() built-in functions.


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Coordinates: ({self.x}, {self.y})"


my_point = Point(1, 2)
print(my_point)

###  __repr__()
# Used to provide a formal representation of the object meant for developers.
# They are used for debugging.
# Called by the repr() built-in function.


class Shirt:
    def __init__(self, color, size, brand):
        self.color = color
        self.size = size
        self.brand = brand

    def __str__(self):
        return f"Color: {self.color}; Size: {self.size}; Brand: {self.brand}"

    def __repr__(self):
        return f'Shirt("{self.color}", "{self.size}", "{self.brand}")'


shirt = Shirt("Blue", "XL", "Retro Land")
print("__str__() -", str(shirt))
print("\n__repr__() -", repr(shirt))

# The object can be recreated if needed
new_shirt = eval(repr(shirt))
print("\n(New object)", new_shirt)

# Notice how the __str__() representation is more "informal" and how the __repr__() representation is much more formal
# (it is a copy of the Python expression used to recreate the object).
# Using the eval() function, we can use the string returned by repr() to recreate the object.

### __len__() ###
# has no default implementation
# we can provide a custom functionality
# has to return an integer


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Coordinates: ({self.x}, {self.y})"

    def __len__(self):
        """Distance from the origin (0,0) rounded to the nearest integer"""
        return round((self.x ** 2 + self.y ** 2) ** (1 / 2))


my_point = Point(1, 2)
len(my_point)

### __getitem__ ###
# used when you try to index the intance of the class


def __getitem__(self, position):
    self.clients[position]


### __add__ ###
# used in addition of instances of the class

my_point = Point(1, 2)
my_point2 = Point(2, 1)
my_point + my_point2  # returns an error

### add __add__() method
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Coordinates: ({self.x}, {self.y})"

    def __len__(self):
        """Distance from the origin (0,0) rounded to the nearest integer"""
        return round((self.x ** 2 + self.y ** 2) ** (1 / 2))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return f"Point: ({x}, {y})"


my_point = Point(1, 2)
my_point2 = Point(2, 1)
my_point + my_point2  # works


### __bool__ ####
# --> bool()
# If a class defines neither __len__() nor __bool__(), all its instances are considered true
# When __bool__() is not defined, __len__() is called, if it is defined, and the object is considered true if its result is nonzero.


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Coordinates: ({self.x}, {self.y})"

    def __len__(self):
        """Distance from the origin (0,0) rounded to the nearest integer"""
        return round((self.x ** 2 + self.y ** 2) ** (1 / 2))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return f"Point: ({x}, {y})"

    def __bool__(self):
        return (self.x + self.y) > 5


my_point = Point(1, 5)
my_point2 = Point(2, 1)
bool(my_point)
bool(my_point2)

### Rich comparison methods ###
# __lt__() less than
# __le__() less or equal
# __eq__() equal
# __ne__() not equal
# __gt__() greater than
# __ge__() greater thanor equal