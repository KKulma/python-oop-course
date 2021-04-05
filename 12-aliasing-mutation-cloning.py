#### ALIASING
## same memory object can be accessed using different names - different names, same subject
a = [1, 4, 6]
b = a
c = b
d = c
a is b is c is d


### MUTABILITY
# mutation - a permanent change
# mutable - object can be changed after it's created
# immutable - object can NOT be changed after it's created

## MUTABLE OBJECTS
# lists
# sets
# distionaries
# advantages - more memory efficient (reuse the existing object instead of creating a new copy for every change); represrnt real-world objects thta are mutable by nature (e.g. player can change speed, location, etc.)
# disadvantages - are more likely to introduce bugs (you can accidentlly change the object)

a = [1, 5, 6, 9]  # a mutable list
a[2] = 7
a


## IMMUTABLE OBJECTS
# booleans
# integers
# floats
# strings
# tuples
# advantages - safer from bugs; easier to understand (no hidden or unexpcted changes to an object)
# disadvantages - less memory efficient (can be costly if an object that we create a copy is big or complex)

t = (1, 5, 6, 9)  # an immutable tuble
t[2] = 7
t

### Be Careful: Built-in Methods can Mutate Objects
# You have to be very careful with built-in methods because some of them mutate the original object.
# For example:

a = [6, 2, 7, 1]
a.sort()
a

# Here you can see (above) that the .sort() method mutated the original list.
# To achieve this same functionality without mutating the original object, you should use the sorted() function.

a = [6, 2, 7, 1]
sorted(a)  # [1, 2, 6, 7]
a  # [6, 2, 7, 1]

# As you can see, this function returns a sorted "version" of the list (a copy) without modifying the original list.
# You can check if a method mutates the object in the official Python documentation

### Important Tip: Immutable doesn't mean that its elements are immutable
# A very important distinction for immutable objects is that they can contain mutable objects, and these mutable objects can be modified even if the container cannot be modified.
# Here is an example that illustrates this. We have this initial list:

a = ([1, 2, 3], "abc", 56)

# If we try to change an element of the tuple, we get an error because tuples are immutable objects:
# But... if we try to modify an element of the tuple that is mutable, we won't get any errors.

a[0][1] = 4
a


#### CLONING
a = [2, 5, 7, 9]
b = a  # craates an alias to the same object
b = a[:]  # CLONING - creates an independent copy of an object
b[0] = 0
a
b

### Shallow VS Deep copy of an object
# When you make a SHALLOW copy of an object, you are making a new object in memory, a new reference, but the content of the object will still point to the same objects.

# by ref
a = ([0, 6, 2], "Hello", 56)
b = a[:]  # shallow copy
b[0][0] = -1
a
b

# by copy() method
a = {"Nora": ["055-452-322", "Washington Ave."], "Gino": ["006-545", "5th Avenue"]}
b = a.copy()
b["Nora"][0] = "56"
b
a

# by copy module
import copy

a = ([5, 2, 6, 2], "Welcome", 67)
b = copy.copy(a)
b[0][0] = -1
a
b

# With a DEEP copy, in addition to creating a copy of the "container" object, you also create a copy of the elements contained in the object.

# with copy module
import copy

a = ([5, 2, 6, 2], "Welcome")
b = copy.deepcopy(a)
b[0][0] = -1
a
b