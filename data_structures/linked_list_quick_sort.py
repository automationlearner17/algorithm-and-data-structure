#!/usr/bin/python3

from linkedlist import Linkedlist
from linkedlist import Node

def quick_sort(list):
  len = list.size()
  if len <= 1:
   return list

  pivot = list.head.data
  current = list.head
  next = current.next_node
  lesser = Linkedlist()
  greater = Linkedlist()
  

  for i in range(1,len):
   if pivot < next.data:
     greater.add(next.data)
     next = next.next_node
   else:
     lesser.add(next.data)
     next = next.next_node
  greter_list = quick_sort(greater)
  lesser_list = quick_sort(lesser)

  return connect(lesser_list,pivot,greter_list)









def connect(list1,node,list2):
     """
      it will connect lists together
     """

     current1 = list1.head
     current2 = list2.head
     size1 = list1.size()
     size2 = list2.size()
     new_list = Linkedlist()
     pivot_list = Linkedlist()
     if size1 == 0 and size2 ==0:
       new_node = Node(node)
       pivot_list.head = new_node
       new_list.head = pivot_list.head
     elif size1 == 0 and size2 == 1:
       new_node = Node(node)
       pivot_list.head = new_node
       new_list.head = pivot_list.head
       new_list.head.next_node = current2
     elif size1 == 1 and size2 == 0:
       new_node = Node(node)
       pivot_list.head = new_node
       new_list.head = current1
       new_list.head.next_node = pivot_list.head
     elif size1 == 1 and size2 == 1:
       new_node = Node(node)
       pivot_list.head = new_node
       new_list.head = current1
       new_list.head.next_node = pivot_list.head
       pivot_list.head.next_node = current2
     elif size1 == 0 and size2 > 1:
       new_node = Node(node)
       pivot_list.head = new_node
       new_list.head = pivot_list.head
       pivot_list.head.next_node = current2
     elif size1 > 1 and size2 == 0:
       new_node = Node(node)
       pivot_list.head = new_node
       new_list.head = current1
       new_list_current = new_list.head
       new_list_size = new_list.size()
       for i in range(1,new_list_size):
           new_list_current = new_list_current.next_node
       new_list_current.next_node = pivot_list.head
     else:
       new_node = Node(node)
       pivot_list.head = new_node
       new_list.head = current1
       new_list_current = new_list.head
       new_list_size = new_list.size()
       for i in range(1,new_list_size):
         new_list_current = new_list_current.next_node
       new_list_current.next_node = pivot_list.head
       pivot_list.head.next_node = current2

     return new_list




l = Linkedlist()
l.add(300)
l.add(400)
l.add(2)
l.add(30)
l.add(0)
l.add(1000)

result = quick_sort(l)
print(result)

  
