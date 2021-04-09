# methods and formats to organise data

## Nodes in data structures
# node - a basic unit of a data structure, contains info on data and connections
# pointer - a reference to aonther node in the data structure


class Node:
    def __init__(self, value, next_node=None):
        self._value = value
        self._next = next_node

    @property
    def value(self):
        print("value getter")
        return self._value

    @value.setter
    def value(self, new_value):
        print("value setter")
        self._value = new_value

    @property
    def next(self):
        print("next getter")
        return self._next

    @next.setter
    def next(self, new_next):
        print("next setter")
        self._next = new_next


node_d = Node("d")
node_c = Node("c", next_node=node_d)
node_b = Node("b", next_node=node_c)
node_a = Node("a", next_node=node_b)

print(node_a.next is node_b)
print(node_a.next)
node_a.next = node_c

### Linked Lists
# a linear collection of data elements that are made of nodes connected to each other
# can store data in continuous places in memory (unlike arrays, for example)
# head - the forst node of the linked list
# tail - the last one

# doubly linked lists - linked from head to tail and from tail to head


class LinkedList:
    def __init__(self):
        self.head = None

    # insert a node at the beginning
    def insert_node(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        elif self.head.value >= value:
            new_node.next = self.head
            self.head = new_node
        else:
            previous = self.head
            runner = self.head.next

            while (runner is not None) and (value > runner):
                previous = runner
                runner = runner.next

            new_node.next = runner
            previous.next = new_node

    # inster the node as tail

    def print_list_item(self):
        if self.head is None:
            print("Empty")
        else:
            runner = self.head
            while runner is not None:
                print(runner.value, end="\n")
                runner = runner.next
            print()
