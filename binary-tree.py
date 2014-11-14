class Node:
    def __init__(self, text):
        self.data = text
        self.left = None
        self.right = None

class BinaryTree:
    root = None

    def insert(self, text):
        if not self.root:
            self.root = Node(text)
        else:
            self.set_next_node_position(text)

    def set_next_node_position(self, text, node=None):
        if not node:
            node = self.root
        if node.data > text:
            if not node.left:
                node.left = Node(text)
            else:
                self.set_next_node_position(text, node.left)
        else:
            if not node.right:
                node.right = Node(text)
            else:
                self.set_next_node_position(text, node.right)
    def print_tree(self, node=None):
        if not node:
            node = self.root
        if node.left:
            self.print_tree(node.left)
        print(node.data)
        if node.right:
            self.print_tree(node.right)

tree = BinaryTree()

tree.insert('f')
tree.insert('c')
tree.insert('b')
tree.insert('e')
tree.insert('h')

tree.print_tree()

pass