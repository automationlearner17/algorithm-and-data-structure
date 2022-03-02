#!/usr/bin/python3

from linkedlist import Linkedlist

def linear_search(list,target):
    current = list.head
    size = list.size()
    for i in range(0,size):
       if current.data == target:
         return True
       else:
         current = current.next_node

    return False

l = Linkedlist()
l.add(10)
l.add(50)
result = linear_search(l,100)
print(result)
