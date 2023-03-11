

class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self._size = 0

    def enqueue(self, item):
        self._size += 1
        node = Node(item)

        if self.rear is None:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node

    def dequeue(self):
        if self.front is None:
            raise IndexError('pop from empty')
        self._size -= 1
        temp = self.front 
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return temp.data

    def size(self):
        return self._size


A = Queue()
A.enqueue(5)
print(A.front is A.rear)
A.enqueue(7)
print(A.front is A.rear)
A.enqueue(11)
print(A.size())
for _ in range(3):
    print(A.dequeue())
