### Why multiple files?
# modules - Ptython files with related classes, method, functions, objects, etc.
# modules should have short lowercase names, underscore can be used to imporve readability


## import statements
# ALWAYS at the top of the file
# in this order: 1. standard library imports, 2. related third party imports, 3. local application/library imports
# put a blank line between different types of imports

# import entire module: import <module>
# import a specific element of the module: import <module>.<element>

import math
math.sqrt(12)

from math import sqrt
sqrt(12)

# wildcard import below is not recommended as it's not clear what names get imported from the module
from <module> import *
<element1>
<element2>

import <module> as <name>
import pandas as pd

# yes:
import os
import sys

# no:
import sys, os

# it's ok for ipmorting multiple elements
from subprocess import Popen, PIPE

### types of imports 
## 🔸 Absolute Imports
# They contain the full path to your script (python file), starting from the root folder.
# The folders are separated with a period.
# It can be as long as needed.
# Advantage: They are the preferred type of import statement because they clearly show the path to the module.
# Disadvantage: They can be quite long if the project has many subfolders.

from <package>.<module> import <module>
import <package>.<module>.<function>

## 🔹 Relative Imports
# The path specifies where the modules are located relative to the current code file.
# The syntax uses leading dots: one dot indicates the directory of the current script. Two dots indicate the parent directory. Three dots indicate the grandfather directory, and so on, one directory per dot.
# For relative imports, the dots can go up to the directory that contains the script that is run.

import other
from .<module> import <element>
from ..<subpackage>.<module> import <element>