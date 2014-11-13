class Node:
    next = None
    data = None


class SingleLinkedList:
    head = None

    def insert(self, obj):
        node = Node()
        node.data = obj

        if not self.head:
            self.head = node
        else:
            self.last_node(self.head).next = node

    def last_node(self, check_node):
        if not check_node.next:
            return check_node
        else:
            return self.last_node(check_node.next)

people = SingleLinkedList()
people.insert('Bob')
people.insert('Sarah')
people.insert('Linda')
pass