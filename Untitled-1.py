# 1. Array (Midterm)
arr = [1, 2, 3, 4, 5]
print("Array:", arr)

# 2. List (Midterm)
my_list = [10, 20, 30, 40, 50]
print("List:", my_list)

# 3. Linked List (Midterm)
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
print("Linked List:")
ll.display()

# 4. Python Class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f"Hello, my name is {self.name}, and I am {self.age} years old.")

person = Person("Alice", 25)
person.say_hello()

# 5. Built-in Queue
from queue import Queue

q = Queue()
q.put(1)
q.put(2)
q.put(3)
print("Queue (FIFO):", q.get(), q.get(), q.get())

# 6. Built-in Stack
from queue import LifoQueue

s = LifoQueue()
s.put(1)
s.put(2)
s.put(3)
print("Stack (LIFO):", s.get(), s.get(), s.get())

# 7. Graph
# Placeholder for Graph

# 8. Queue on Linked List
# Placeholder for Queue implemented with Linked List

# 9. Stack on Linked List
# Placeholder for Stack implemented with Linked List

# 10. Binary Search Tree
# Placeholder for Binary Search Tree

# 11. Doubly Linked-List
# Placeholder for Doubly Linked-List

# 12. Dictionary (Midterm)
my_dict = {"apple": 3, "banana": 2, "cherry": 5}
print("Dictionary:", my_dict)
