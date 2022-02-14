#!/usr/bin/python3

from linkedlist import Linkedlist
from linkedlist import Node
import sys
import random

def is_sorted(list):
  size = list.size()
  if size <= 1:
   return list
  
  current = list.head
  next = current.next_node

  for i in range(1,size):
    first = current.data
    second = next.data
    if first < second:
     return False
    else:
      current = current.next_node
      next = next.next_node
      

  return True


def bogo_sort(list):
   if is_sorted(list) == True:
     return list
   else:
     ne_ar = rearng(list)
     random.shuffle(ne_ar)
     new_linked = make_linked_list(ne_ar)
     while is_sorted(new_linked) == False:
        ne_ar = rearng(new_linked)
        random.shuffle(ne_ar)
        new_linked = make_linked_list(ne_ar)
  

   return new_linked

def rearng(list):
  ar = []
  ln = list.size()
  current = list.head
  for i in range(0,ln):
    
    ar.append(current.data)
    current = current.next_node
  return ar

def make_linked_list(ar):

 new_linked = Linkedlist()
 current = new_linked.head
 for i in ar:
   new_linked.add(i)

 return new_linked
 





     
l = Linkedlist()
l.add(200)
l.add(100)
l.add(600)
#l.add(3)
#l.add(67)



result = bogo_sort(l)
print(result)

