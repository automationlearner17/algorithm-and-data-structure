#!/usr/bin/python3

from linkedlist import Linkedlist

def binary_search(list,target):
   find = 0
   target_not_found = 0

   while find == 0 and target_not_found == 0:
     size = list.size()
     if size == 1:
       if list.head.data == target:
          find = 1
       else:
          target_not_found = 1
     mid = size // 2
     mid_node = list.find_node(mid)
     if mid_node.data == target:
       find = 1
     else:
       if mid_node.data > target:
          end = mid - 1
          last_node = list.find_node(end)
          last_node.next_node = None

       else:
          first = mid + 1
          first_node = list.find_node(first)
          if first_node != None:
            list.head = first_node
          else:
            target_not_found = 1

   if target_not_found == 1:
        find = 0
   if find == 0:
     find = False
   else:
      find = True     

   return find
   


l = Linkedlist()
l.add(180)
l.add(100)
l.add(74)
l.add(55)
l.add(30)
l.add(1)
l.add(0)
result = binary_search(l,30)
print(result)
   
