__author__ = 'adambarnhard'

class Queue1:
    data = []

    def enqueue(self, name):
        self.data.append(name)

    def dequeu(self):
        return self.data.pop(0)

