#!/usr/bin/python3

from linkedlist import Linkedlist
from linkedlist import Node

def selection_sort(list):
  sorted_list = Linkedlist()
  size = list.size()
  while size > 0:
    min_value = min_value_method(list)
    if sorted_list.size() < 1:
      sorted_list.add(list.remove(min_value))
      size = size - 1
    else:
      len = sorted_list.size()
      current = sorted_list.head
      if len > 1:
       for i in range(1,len):
         current = current.next_node
   
      node = Node(list.remove(min_value))
      current.next_node = node
      size = size - 1

  return sorted_list

def min_value_method(list):
    length = list.size()
    current = list.head
    next = current.next_node
    minimum = 0
    if length == 1:
     minimum = current.data
    else:
     for i in range(1,length):
       if current.data < next.data:
        minimum = current.data
        next = next.next_node
       else:
        minimum = next.data
        current = next
        next = next.next_node
        

    return minimum

l = Linkedlist()
l.add(100)
l.add(4)
l.add(50)
l.add(22)
l.add(1000)

values = selection_sort(l)
print(values) 
      
     
       
