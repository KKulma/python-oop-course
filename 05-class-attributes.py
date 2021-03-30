# belong to the class and are sahred between all the class instances 
# usually located at the top of the class 

class Donut:
    
    init_price = 3 #class attribute
    
    def __init__(self, flavor, toppings, filling, size): # class instance attributes     
        self.flavor = flavor
        self.toppings = toppings
        self.filling = filling
        self.size = size
        

class Quadruoed:
    num_feet = 4
    
    def __init__(self, domain, species):
        self.domain = domain
        self.species = species

Quadruoed.num_feet = 44
Quadruoed.num_feet

class A:
    attr1 = 5
    
    def __init__(self):
        A.attr1 += 1
 
a1 = A()
a2 = A()
A.attr1 = 26
a3 = A()
A.attr1