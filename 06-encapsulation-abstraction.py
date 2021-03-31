# ENCAPSULATION - bundling of data and methods that act on that data into a single unit (class)
# public and non-public ("private") attributes
# getters and setters

# ABSTRACTION - the interface (user's view) of the components should be independent of the implementation (developer's view)

## PRIVATE AND PUBLIC ATTRIBUTES
# public attributes can be accessed everywhere
# private (non-public) can't/shouldnt be accessed outside the class -- there are 2 levels of access restrictions

## NON-PUBLIC RESTRICTIONS
# protected: _<attribute>
# private (name mungling): __<attribute>

class Car: 
    def __init__(self, model, year, id_num, engine_serial_num):
        self.model = model
        self.year = year
        self._id_num = id_num
        self.__engine_serial_num = engine_serial_num
        
my_car = Car("Fiesta", 2006, 12345, 1234567890)
my_car.model
# my_car.id_num # doesn't exist
my_car._id_num # protected attribute can be accessed 
my_car.__engine_serial_num ## privatae attribute can't be accessed the same way as the private one 
# my_car._Car__engine_serial_num ## private attribute CAN be accessed via the name mungling, though


class Book:
 
	def __init__(self, title, author, num_pages, ISBN, publisher):
		self.title = title
		self.author = author
		self._num_pages = num_pages
		self._ISBN = ISBN
		self.publisher = publisher
