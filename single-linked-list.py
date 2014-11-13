class Node:
    # __init__ is the constructor function for python
    def __init__(self, data):
        self.next = None
        self.data = data


class SingleLinkedList:
    head = None

    def insert(self, obj):

        if not self.head:
            self.head = Node(obj)
        else:
            self.last_node().next = Node(obj)

    def last_node(self, node=None):
        if not node:
            node = self.head
        if not node.next:
            return node
        else:
            return self.last_node(node.next)


people = SingleLinkedList()
people.insert('Bob')
people.insert('Sarah')
people.insert('Linda')
pass