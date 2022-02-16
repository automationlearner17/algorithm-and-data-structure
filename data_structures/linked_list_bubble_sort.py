#!/usr/bin/python3

from linkedlist import Linkedlist

def bubble_sort(list):

  size = list.size()
  for i in range(0,size):
   list = swping(list)

  return list

def swping(list):

  len = list.size()
  current = list.head
  next = current.next_node

  for i in range(1,len):
    if current.data > next.data:
      swipe = next.data
      replace = current.data
      current.data = swipe
      next.data = replace
      current = next
      next = next.next_node
    else:
      current = next
      next = next.next_node

  return list

l = Linkedlist()
l.add(200)
l.add(500000)
l.add(6)
l.add(3)
l.add(100)

result = bubble_sort(l)

print(result)
