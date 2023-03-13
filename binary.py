class BinaryTree:
    def __init__(self, value):
        self.key = value
        self.left_child = None
        self.right_child = None
        

    def insert_left(self, value):
        if self.left_child == None:
            self.left_child = BinaryTree(value)
        else:
            bin_tree = BinaryTree(value)
            bin_tree.left_child = self.left_child
            self.left_child = bin_tree

    def insert_right(self, value):
        if self.right_child == None:
            self.right_child = BinaryTree(value)
        else:
            bin_tree = BinaryTree(value)
            bin_tree.right_child = self.right_child
            self.right_child = bin_tree

    def breadth_first_search(self, n):
        current = [self]
        next = []
        while current:
            for node in current:
                if node.key == n:
                    return True
                if node.left_child:
                    next.append(node.left_child)
                if node.right_child:
                    next.append(node.right_child)
            
            current = next
            next = []
        return False
    
    def invert(self):
        current = [self]
        next = []
        while current:
            for node in current:
                if node.left_child:
                    next.append(node.left_child)
                if node.right_child:
                    next.append(node.right_child)
                node.left_child, node.right_child = node.right_child, node.left_child
            current = next
            next = []


    def has_leaf_nodes(self):
        has_left = False
        has_right = False
        current = [self]
        next = []
        bool_stuff = []
        while current:
            for node in current:
                if node.left_child:
                    next.append(node.left_child)
                    if node.left_child and node.right_child:
                        has_left = True
                if node.right_child:
                    next.append(node.right_child)
                    if node.right_child and node.left_child:
                        has_right = True
            bool_stuff.append(not(has_left & has_right))
            has_left = False
            has_right = False
            current = next
            next = []
        print(bool_stuff)
        return bool_stuff[-2]



    

def invertTree(root):

    if root:
        root.left_child, root.right_child = invertTree(root.right_child), invertTree(root.left_child)
        return root

def preoder(tree):
    if tree:
        print(tree.key)
        preoder(tree.left_child)
        preoder(tree.right_child)




a = BinaryTree(5)

a.insert_left(7)
a.insert_right(11)
a.insert_left(4)
a.left_child.insert_right(3)
a.insert_right(21)
print(preoder(a))
print(preoder(invertTree(a)))
