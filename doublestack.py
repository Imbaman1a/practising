class Deque:
    def __init__(self):
        self.stack_1 = []
    
    def push(self, data):
        self.stack_1.append(data)

    def pull(self):
        if self.stack_1:
            return self.stack_1.pop(0)
        else: 
            return 'error'


a = Deque()
a.push(5)
a.push(7)
a.push(11)

for _ in range(4):
    print(a.pull())



