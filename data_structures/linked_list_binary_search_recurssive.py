#!/usr/bin/python3

from linkedlist import Linkedlist

def binary_search(list,target):
    size = list.size()
    if size == 1:
      if list.head.data == target:
            return True
      else:
            return False
    else:
     mid = size // 2
     mid_node = list.find_node(mid)
     if mid_node.data == target:
       return True
     else:
         if mid_node.data > target:
             end = mid - 1
             last_node = list.find_node(end)
             last_node.next_node = None
             return binary_search(list,target)
         else:
             first = mid + 1
             first_node = list.find_node(first)
             if first_node is None:
                 return False
             list.head = first_node
             return binary_search(list,target)



l = Linkedlist()
l.add(100)
l.add(90)
l.add(80)
l.add(70)
l.add(60)
l.add(50)

result = binary_search(l,40)
print(result)
