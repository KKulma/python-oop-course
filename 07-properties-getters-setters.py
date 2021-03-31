#### GETTERS AND SETTERS
# they are methods (actions)
# their purpose is to get and set the value of an instance attribute
# they protect data by providing an indirect way to access and modify it

### GETTERS
# indirict way of accessing an attribute
# get_ + <attribute>s


class Dog:
    def __init__(self, name):
        self._name = name  # protected attribute

    def get_name(self):  # getter, usuallly has one parameter self
        return self._name


dog = Dog("Nora")
dog.get_name()

### SETTERS
# indirect way of modifying an attribute
# you can validate the new value before you assign it to the protected attribute
# set_ + <attribute>


class Dog2:
    def __init__(self, name):
        self._name = name  # protected attribute

    def get_name(self):  # getter, usuallly has one parameter self
        return self._name

    def set_name(self, name):  # setter,
        if isinstance(name, str):  # check if the new name is a string
            self._name = name
        else:
            print("Please, enter a valid name")


dog1 = Dog2("Nora")
dog1.set_name(123)
dog1.set_name("Emily")
dog1.get_name()


## PROPERTIES = PYTHONIC WAY OF CREATING GETTERS AND SETTERS
# way of connecting attributes with their getters and setters


class Dog3:
    def __init__(self, name):
        self._name = name  # protected attribute

    def get_name(self):  # getter, usuallly has one parameter self
        return self._name

    def set_name(self, name):  # setter,
        if isinstance(name, str):  # check if the new name is a string
            self._name = name
        else:
            print("Please, enter a valid name")

    age = property(get_name, set_name)  # property


# @property decorator
# avoid calling property()
# avoid namespace pollution (no get_<attr> or set_<attr>)
# decorator = a function that takes a function as argument to extend its functionality without actually modifying it


class Dog4:
    def __init__(self, age):
        self._age = age  # protected attribute

    @property
    def age(self):
        print("Running getter")
        return self._age

    @age.setter
    def age(self, new_age):
        print("Running setter")
        if isinstance(new_age, int) and 0 < new_age < 30:
            self._age = new_age
        else:
            print("Please enter a valid age")

    @age.deleter  # deleter!
    def age(self):
        print("Deleter")
        del self._age

    final_dog = Dog4(12)
    final_dog.age
    final_dog.age = 31
    final_dog.age = 16
    del final_dog.age


### Assignment
class BouncyBall:
    def __init__(self, price, size, brand):
        self._price = price
        self._size = size
        self._brand = brand

    @property
    def price(self):
        print("Price getter")
        return self._price

    @property
    def size(self):
        print("Size getter")
        return self._size

    @property
    def brand(self):
        print("Brand getter")
        return self._brand

    @price.setter
    def price(self, new_price):
        if isinstance(new_price, int):
            print("Setter")
            self._price = new_price
        else:
            print("Price must be integer")

    @size.setter
    def size(self, new_size):
        if isinstance(new_size, int):
            print("Setter")
            self._size = new_size
        else:
            print("Size must be integer")

    @brand.setter
    def brand(self, new_brand):
        if isinstance(new_brand, str):
            print("Setter")
            self._brand = new_brand
        else:
            print("Brand must be character string")


bb = BouncyBall(12, 1, "Pyku")
bb.brand = "Mine"
bb.size = 12
bb.price = 2