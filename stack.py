class Node:
    def __init__(self, data, Next = None):
        self.data = data
        self.Next = Next


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            return 
        current = self.head
        while current.Next:
            current = current.Next
        current.Next = Node(data)

    def search(self, target):
        current = self.head
        while current.Next:
            if current.data == target: return True
            else: current = current.Next
        return False
    
    def remove(self, target):
        if self.head.data == target:
            self.head = self.head.Next
            return 
        
        current = self.head
        previous = current

        while current:
            if current.data == target:
                previous.Next = current.Next
            previous = current
            current = current.Next
    
    def reverse_list(self):
        current = self.head
        previous = None
        while current:
            Next = current.Next
            current.Next = previous
            previous = current
            current = Next
        self.head = previous
    
    def detect_cycle(self):
        slow = self.head
        fast = self.head

        while True:
            try:
                slow = slow.Next
                fast = fast.Next.Next
                if slow is fast:
                    return True
            except:
                return False


    def __str__(self):
        node = self.head
        while node is not None:
            print(node.data)
            node = node.Next
        return 'End of List'
        
class MaxStack:
    def __init__(self):
        self.main = []
        self.max = []

    def push(self, data):
        if len(self.main) == 0:
            self.max.append(data)
        elif data > self.max[-1]:
            self.max.pop()
            self.max.append(data)
        self.main.append(data)

    def pop(self):
        return self.main.pop()

    def get_max(self):
        return self.max[-1]

def checkBalance(a_string: str) -> bool:
    if not a_string: return False
    else:
        stack = [] 
        for c in a_string:
            if c == '(' or c == '{':
                stack.append(c)
            elif c == ')' or c == '}':
                try:
                    stack.pop()
                except:
                    return False
    return len(stack) == 0


a_list = LinkedList()

a_list.append('Monday')
a_list.append('Tuesday')
a_list.append('Wendesday')
print('Final list:', a_list)

lst = MaxStack()
lst.push(1)
lst.push(3)
lst.push(0)
a = 'ksfkgaa(ksfldf)l;sdlfl(lksdg{});sk'
print(checkBalance(a))
#a_list.reverse_list()
