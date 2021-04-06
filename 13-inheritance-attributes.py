#### INHERITANCE
# reusibility (avoid code duplication)
# extensibility (create more specific classes inheriting from more general classes)
# child class (subclass) inherits from the parent class (superclass)

# parent class Employee
class Employee:

    salary = 100000
    monthly_bonus = 500

    def __init__(self, name, age, address, phone):
        self.name = name
        self.age = age
        self.address = address
        self.phone = phone


# Inherits from Employee
class Programmer(Employee):  # indication of inheritance
    def __init__(self, name, age, address, phone, programming_languages):
        Employee.__init__(
            self, name, age, address, phone
        )  # parent class initialization
        self.programming_languages = (
            programming_languages  # plus subclass-specific init
        )


# Inherits from Employee
class Assistant(Employee):
    def assistant_intro(
        self,
    ):  # we don't need an init step, it's inherited from Employee
        print("Hello! My name is {self.name} and I'm an assistant!")


### Check if a Class is a Subclass of another Class
issubclass(Assistant, Employee)


### How to use "super" to refer to the superclass
## super()
# This is a built-in Python function that is used to refer to the immediate parent class of the current class.
# > "In a class hierarchy with single inheritance, super can be used to refer to parent classes without naming them explicitly, thus making the code more maintainable. This use closely parallels the use of super in other programming languages." — source: Built-in Functions - Python Documentation

## Alternative Syntax
# You can use super() in __init__() to make your subclass inherit the attributes of the superclass.
# For example:


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Poodle(Dog):
    def __init__(self, name, age, code):
        super().__init__(name, age)
        self.code = code


# This line:

super().__init__(self, name, age)
# is equivalent to the syntax that you learned in the previous video:

Dog.__init__(self, name, age)
# 💡 Note: for this new syntax, you do not need to pass self as the first argument. You only pass the other arguments.


### ASSIGNMENT
class Mammal:
    def __init__(self, name, age, health, num_offspring, years_in_captivity):
        self.name = name
        self.age = age
        self.health = health
        self.num_offspring = num_offspring
        self.years_in_captivity = years_in_captivity


# Define the Panda class below this line


class Panda(Mammal):
    is_endangered = True

    def __init__(self, name, age, health, num_offspring, years_in_captivity, code):
        Mammal.__init__(
            self, name, age, health, num_offspring, years_in_captivity
        )  # parent class initialization
        self.code = code


my_panda = Panda("Kasia", 2, "Excellent", 0, 1, "123")

#### Multilevel Inheritance
# Multilevel inheritance is different from multiple inheritance, in which a class is derived from more than one parent class.
class Vehicle:
    pass


class LandVehicle(Vehicle):
    pass


class Car(LandVehicle):
    pass


class Truck(LandVehicle):
    pass


### Multiple Inheritance
# In multiple inheritance, a class has more than one parent class.
# For example, if you are developing a GUI (Graphical User Interface), a Button class could inherit from both the Rectangle class (for style) and from the GUIEelement class (for functionality).


class Rectangle:
    def __init__(self, length, width, color):
        self.length = length
        self.width = width
        self.color = color


class GUIElement:
    def click(self):
        print("The object was clicked...")


class Button(Rectangle, GUIElement):  # indicate multiple inheritance
    def __init__(self, length, width, color, text):
        Rectangle.__init__(self, length, width, color)
        self.text = text


### ASSIGNMENT
class Pizza:
    def __init__(self, size, toppings, price, rating):
        self.size = size  # "Small", "Medium", or "Large"
        self.toppings = toppings  # A list of toppings
        self.price = price
        self.rating = rating  # Scale from 1 to 5


# Add the subclasses below this line
class PizzaMargerita(Pizza):
    def __init__(self, size, toppings, price, rating, has_extra_cheese):
        Pizza.__init__(self, size, toppings, price, rating)
        self.has_extra_cheese = has_extra_cheese


class PizzaMarinara(Pizza):
    def __init__(self, size, toppings, price, rating, has_extra_basil):
        Pizza.__init__(self, size, toppings, price, rating)
        self.has_extra_basil = has_extra_basil


margherita = PizzaMargerita(2, None, 12, 5, True)
marinara = PizzaMarinara(2, None, 12, 5, True)
