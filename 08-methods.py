# methods control how an object can exeute operations and interact with its data
# belong to the class not an instance and can modify indicual data of the instances that call them
# they are actions, therefore they names are verbs, lowercase with snake_case
# def <method_name>(self, <params>):


class Calculator:
    def __init__(self, model, year, serial_num):
        self.model = model
        self.year = year
        self.__serial_num = serial_num

    def display_data(self):
        print(f"Model: {self.model}; Year: {self.year}")

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        if a >= b:
            return a - b
        else:
            raise ValueError("a has to be greater than b")

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            raise ValueError("b has to be greater than 0")


calc1 = Calculator("Siemens", 2006, 12345)
calc1.display_data()
calc1.add(3, 4)
calc1.subtract(3, 4)
calc1.subtract(b=3, a=4)
calc1.divide(3, 4)
calc1.multiply(3, 4)

# another way of applying a method to an instance
calc2 = Calculator("Siemens", 2006, 12345)
Calculator.add(calc2, 1, 2)

### NON-PUBLIC METHOD AND NAME MUNGLING

# def _display_data # protected method
# def __display_data # private mothod - name mungling applies

### DEFAULT ARGUMENTS
# def <method_name>((self, <param>, ..., <param>=<value>))

### CALL METHODS FROM OTHER METHODS
# self.method_name(<args>)
# example of how to refer to other methods in the class


class CashRegister:
    tax = 0.05

    def __init__(self, cashier, serial):
        self.cashier = cashier
        self.__serial = serial

    def display_total(self, subtotal):
        print("The subtotal is: ", subtotal)
        print("The tax is: ", self.calculate_tax(subtotal))
        print("The total is:", self.calculate_total(subtotal))

    def calculate_total(self, subtotal):
        return subtotal + self.calculate_tax(subtotal)

    def calculate_tax(self, amount):
        return amount * CashRegister.tax


### RETURN STATEMENTS
# You can return values from methods just like you return values from functions, with return statements.
# Here we have an example. This is a Calculator class.


class Calculator:
    def add(self, a, b):
        print(a + b)

    def multiply(self, a, b):
        return a * b


# The add() method prints the value, it doesn't return it.
# The multiply() method does return the value.

# When the add() method is called, the value is printed, but None is returned. This exactly what you would expect from a regular function that doesn't have a return statement.
# When the multiply() method is called, the value is returned.

calculator = Calculator()
calculator.add(5, 6)
print(calculator.add(5, 6))
calculator.multiply(5, 6)
print(calculator.multiply(5, 6))

### METHOD CHAINING
# In Object-Oriented Programming, Method Chaining is a very common syntax that lets us call several methods one after the other on the same instance.


class Pizza:
    def __init__(self):
        self.toppings = []

    def add_topping(self, topping):
        self.toppings.append(topping.lower())
        return self

    def display_toppings(self):
        print("This Pizza has:")
        for topping in self.toppings:
            print(topping.capitalize())


## example of method chaining
pizza = Pizza()
pizza.add_topping("mushrooms").add_topping("olives").add_topping(
    "chicken"
).display_toppings()


## assignments
class Circle:

    pi = 3.1416

    def __init__(self, radius, color):
        self.radius = radius
        self.color = color

    # Add the method below this line
    def find_area(self):
        return Circle.pi * (self.radius) ** 2


blue_circle = Circle(15, "Blue")

# Call the method with blue_circle and assign the result to the variable final_area
blue_circle.find_area()
