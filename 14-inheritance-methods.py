### INTRO TO METHOD INHERITANCE
# include common functionality shared by parent- ad child classes
# when a subclass instance calls a method, it will look for it in subclass and the parent class until the top of the hierarchy is reached
# methods are inherited automatically
# You can call a method from the superclass in the subclass with this syntax:
# <ClassName>.<method_name>(self, <args>) e.g Triangle.find_area(self)
# or
# super().<method_name>(<args>) e.g super().find_area()


class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def find_area(self):
        print((self.base * self.height) / 2)


class RightTriangle(Triangle):
    def display_area(self):
        print("=== Right Triangle Area ===")

        # This line calls the method from the Triangle class
        Triangle.find_area(self)  # You could also use super().find_area()


right_triangle = RightTriangle(5, 6)
right_triangle.display_area()

## ASSIGNMENT
class Professor:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def greet_students(self):
        print("Welcome to class!")


# Define your class below this line
class ScienceProfessor(Professor):
    def __init__(self, name, age, course):
        Professor.__init__(self, name, age, course)

    def greet_students(self):
        print("Hi everyone! It's a great day to study science!")
        Professor.greet_students(self)


science_professor = ScienceProfessor("Kasia", 35, "Biology")
science_professor.greet_students()


### METHOD OVERRIDING


class Teacher:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def welcome_student(self):
        print("Welcome to class!")


# Define your class below this line
class ScienceTeacher(Professor):
    def __init__(self, name, age, course):
        Professor.__init__(self, name, age, course)

    def welcome_student(self):  # method overriding
        print("Hi everyone! It's a great day to study science!")
        Professor.greet_students(self)


### OVERRIDING VS OVERWRITING
# overwriting would indicate that the superclass definition of the method is no longer available
# that's why in above examples we talk about overriding

## ASSIGNMENT
class Store:
    def __init__(self, name, address, num_employees):
        self.name = name
        self.address = address
        self.num_employees = num_employees

    def greet_customers(self):
        print("Welcome to our store! What would you like to buy?")


# Create your DonutStore class below this line
class DonutStore(Store):
    def __init__(self, name, address, num_employees):
        Store.__init__(self, name, address, num_employees)

    def greet_customers(self):
        print("Welcome to our store! What donut would you like to eat?")


my_donut_store = DonutStore("Do", "Pyk", 12)

### METHOD OVERLOADING
# It occurs when two methods in the same class have the same name but different parameters,
# so when you call the method, the version that is executed is determined by the data types of the arguments
# or by the number of arguments.
# Python does not support method overloading!!!
# The closest thing that you could think of in Python is default arguments,
# because you can call a method passing a different number of arguments if you want to use the default values.
# But this is not method overloading per se.

### POLYMORPHISM
# Polymorphism means that an object can take many forms
# Polymorphism can be achieved through method overriding and method overloading (method overloading is not supported in Python per se)
