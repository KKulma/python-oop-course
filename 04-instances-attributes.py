# Instance - a concrete object created from the (abstract) Class blueprint 
# Different instances share the same categories of the attributes but the actual values of the attributes will be different 

# __init__ is a class constructor - it's executed when an instancec is created 

class House:
    def __init__(self, price):
        self.price = price
        

class Client:
    def __init__(self, name, age, code, passport_num):
        self.name = name
        self.age = age
        self.code = code
        self.passport_num = passport_num

class Rectangle: 
    def __init__(self, lenght, width, color):
        self.lenght = lenght
        self.width = width
        self.color = color


class Circle:
    def __init__(self, radius):
        self.something = radius
    

my_rectangle = Rectangle(5, 4, "blue")
my_circle = Circle(8)
my_rectangle.lenght
my_circle.something
# replace the value of the instance attribute
my_circle.something = 10
my_circle.something
 

## None - way to indicate NULL object
isinstance(None, object)
type(None)

### you can omit the arguments when creating an instance 
# optional arguments always have to be at the end of the argument list
class Patient:    
    def __init__(self, name, age, allergies=None, num_children=0):
        self.name = name
        self.age = age
        self.allergies = allergies
        self.num_children = num_children

patient1 = Patient(name = "Kasia", age = 15, allergies = ["Peanut", "Chocolate"])
patient2 = Patient("Basia", 35, "Chocolate", 2)
patient3 = Patient("Asia", 7)
patient1.age


## Assignment 

class Bacteria:
    def __init__(self, shape, env, has_wall, x, y):
        self.shape = shape
        self.env = env
        self.has_wall = has_wall
        self.x = x
        self.y = y
        
bacteria1 = Bacteria("Round", "Water", False, 1, 0)
bacteria2 = Bacteria("Long", "Soil", True, 1, 1)
bacteria3 = Bacteria("Round", "Gut", False, 0, 1)

## Fix the errors

class Donut:
    def __init__(self, flavor, toppings, filling, size):
        self.flavor = flavor
        self.toppings = toppings
        self.filling = filling
        self.size = size

class Customer:
	def __init__(self, name, age, address, favorite_dessert):
		self.name = name
		self.age = age
		self.address = address
		self.favorite_dessert = favorite_dessert

class Cake:
	def __init__(self, flavor, price, quality):
		self.flavor = flavor
		self.price = price
		self.quality = quality
