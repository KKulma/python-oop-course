### docstrings
# human readible comment explaining purpose and logic. data types and other  relevant information about your code
# string literals
# first statement in a class, method, module or function
# should be included for all public methods (includioiong __init__())
# one line or multi-line

# can be read using help(<element>)
# are linked to the element that they describe throughh the __doc__ attribute
# can be converted into documentation

# single line 
''' Adds x and y and returns a list ''''


## multi-line 

## documenting a FUNCTION or a METHOD
# one liner with what it does and what it returns
# more elaborate description
# Args: describes arguments and optional arguments
# Returns: what it returns and what type
# Any side efffects (e.g. mutation)
# Raises: when it returns an error
# restriction on when it can be called 

## documenting a CLASS
# purpose 
# Attributes: class attributess s
# Methods: list public methods
# effects of inheritance 
# __init__() documented seseparately: short one-liner, blank line + the list of rgumants with arg types 
# individual methods documented individually
# for properties, only document the getters - any docstrings added to the setters won't be displayed 

### EXCEPTIONS 
# Exceptions will be mentioned in this section because you should document them in your docstrings.
# Please refer to this article if you would like to read a quick introduction to the concept of exceptions:
# https://docs.python.org/3/tutorial/errors.html

# There are three main styles used to write docstrings:
# Sphinx Style https://sphinx-rtd-tutorial.readthedocs.io/en/latest/docstrings.html#the-sphinx-docstring-format
# Google Style http://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings
# Numpy Style https://numpydoc.readthedocs.io/en/latest/format.html#docstring-standard



### Accessing docstrings with __doc__
 
def add(a, b):
    '''Add two integers and return the resulting integer'''
    return a + b

help(add)
add.__doc__ #returns just docstrings

### other example 
def frequency_dict(data):
    """Return a dictionary with the number of occurrences of each value in the list.
 
    Create a dictionary that maps each element of the list
    to the number of times it occurs in the list.
 
    Args:
        data: A list of values of an immutable data type.
            These values can be integers, booleans, tuples, or strings.
 
    Return:
        A dictionary mapping each value with its frequency.
        For example, this function call:
 
        a = [1, 6, 2, 6, 2]
 
        returns this dictionary:
        {1: 1, 6: 2, 2: 2}
 
    Raises:
        ValueError: if the list is empty.
 
    """
    if not data:
        raise ValueError("The list cannot be empty")
    
    freq = {}
    
    for elem in data:
        if elem not in freq:
            freq[elem] = 1
        else:
            freq[elem] += 1
 
    return freq

frequency_dict.__doc__