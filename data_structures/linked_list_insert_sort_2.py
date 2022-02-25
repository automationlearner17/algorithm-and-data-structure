#!/usr/bin/python3

from linkedlist import Linkedlist
from linkedlist import Node

def insert_sort(list):
  count = 1
  size = list.size()
  for i in range(1,size):
     current = list.head
     next = current.next_node
#     if count == 1:
#      next = current.next_node

     if count > 1:
      for k in range(1,count):
        next = next.next_node

     index = 0
     find = 0

     while count > index and find == 0: 
       if current.data > next.data and current != list.head:
          node = Node(list.remove(next.data))
          previous.next_node = node
          node.next_node = current
          current = list.head
          find = find + 1
       elif current.data > next.data and current == list.head:
          list.add(list.remove(next.data))
          current = list.head
          find = find + 1

     
       previous = current
       current = current.next_node
       index = index + 1

     count = count + 1

  return list

l = Linkedlist()
l.add(10)
l.add(500)
l.add(0)
l.add(7000)
l.add(778787878)
l.add(1)
l.add(888828828282)

result = insert_sort(l)
print(result)
