#!/usr/bin/python3

from linkedlist import Linkedlist
from linkedlist import Node

def insert_sort(list):
   size = list.size()
   new = Linkedlist()

   current = list.head
   
   for i in range(0,size):
      value = list.remove(current.data)
      length = new.size()
      if length < 1:
        new.add(value)
        current = current.next_node
      else:
        new_current = new.head
        privious = None
        node = Node(value)
        index = 0

        while length > index and new_current:
               if new_current.data > value and new_current == new.head:
                   new.add(value)
                   index = length
               elif new_current.data > value:
                   privious.next_node = node
                   node.next_node = new_current
                   index = length
               else:
                  if new_current.next_node == None:
                     new_current.next_node = node
                  
               privious = new_current
               new_current = new_current.next_node
               index = index + 1
        current = current.next_node

   return new


l = Linkedlist()
l.add(700)
l.add(6000)
l.add(3400)
l.add(3)
l.add(888888888)
l.add(537)
result = insert_sort(l)
print(result)
   
             
        
             
           
            
               
