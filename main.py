from stack import *
from queuu import *
from recursion import *

food = Stack()
food.push('hamburger')
food.push('fries')
food.push('cake')
food.pop()

food2 = Queue1()
food2.enqueue('hamburger')
food2.enqueue('fries')
food2.enqueue('cake')

food2.dequeu()

print(fact(5))

for x in range(20):
    print('fib({0}) = {1}'.format(x, fib(x)))