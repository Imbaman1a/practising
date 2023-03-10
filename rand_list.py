import random

class Node:
    def __init__(self, data, pointer = None):
        self.data = data
        self.pointer = pointer


class duList:

    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            return
        current = self.head
        while current.pointer:
            current = current.pointer
        current.pointer = Node(data)

    def __repr__(self):
        current = self.head
        while current:
            print(current.data)
            current = current.pointer


class forList:

    def __init__(self):
        self.head = None

    def insert(self, data):
        if not self.head:
            self.head = Node(data)
            return 
        current = self.head
        while current.pointer:
            current = current.pointer
        current.pointer = Node(data)
        current.pointer.pointer = self.head

    def detect(self):
        slow = self.head
        fast = self.head

        while True:
            try:
                slow = slow.pointer
                fast = fast.pointer.pointer

                if slow is fast: return True

            except:
                return False

a = forList()

a.insert('Monday')
a.insert('Tuesday')
print(a.detect())
