#!/usr/bin/python3

from linkedlist import Linkedlist
from linkedlist import Node

def shell_sort(list):
  """
     In this algorithm we will ixtend the insert sort algprithm in clear way and will 
     try to make our algorithm much efficient then insert sort , Since in insert sort
     we are comparing our element with its addjecient element and we do lot of swipes 
     and comaparitions in order to reduce the number of the comparision or swipes of 
     algorithm we use shell sort in which we compare elements but not its addjicent one
     insted of that we use to compare with far ones elements with providing gap to 
     list and then we reduce the gap one by one and finally we will get shell sort 
     as same as the insert sort and compare the addjicent values 
     time complexity of this aglorithm is squeare of n in case of worst case scenario
     but in real case scenario the time complexity depends on the gaps.
   """

  size =  list.size()
  value = size - 1
  Gap = size // 2
  odd = size / 2
  
  if odd is int:
   while Gap > 0:
     gap = Gap
     current = list.head 
     i = 0
     while value >= gap:
       data = list.find_node(gap)
       if current.data > data.data:
          remove = list.remove(current.data)
          replace = list.remove(data.data)
          list.insert(replace,i)
          list.insert(remove,gap)

       i = i + 1
       gap = gap + 1
       current = current.next_node
     Gap = Gap - 1
  else:
    find = 1
    while Gap >= 0 and find:
       if Gap == 0:
         Gap = 1
         find = 0
       gap = Gap
       current = list.head
       i = 0
       while value >= gap:
          data = list.find_node(gap)
          if current.data > data.data:
            remove = list.remove(current.data)
            replace = list.remove(data.data)
            list.insert(replace,i)
            list.insert(remove,gap)
          i = i + 1
          gap = gap + 1
          current = current.next_node
       Gap = Gap - 1 
    


  return list


l = Linkedlist()
l.add(300)
l.add(97989)
l.add(787)
l.add(47374874)
l.add(0)
l.add(378473847)
l.add(2)


reslut = shell_sort(l)
print(reslut)

   
