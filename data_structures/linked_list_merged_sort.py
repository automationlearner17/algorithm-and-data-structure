#!/usr/bin/python3

from linkedlist import Linkedlist

def merge_sort(linkedlist):
   """
    it will split the linkedlist recurresively and sort those splited list
    and merge those back
   """
   size = linkedlist.size()
   if size == 0 or size == 1:
    return linkedlist

   first_half,second_half = split(linkedlist)

   first = merge_sort(first_half)
   second = merge_sort(second_half)

   return merge(first,second)


def split(linkedlist):

 """
   first we will calculate mid of linked list and then we will split the list
   using mid point
 """
 size = linkedlist.size()
 
 mid = size//2
 mid_node = linkedlist.find_node(mid-1)

 first_half = linkedlist
 second_half = Linkedlist()
 second_half.head = mid_node.next_node
 mid_node.next_node = None

 return first_half,second_half

def merge(first,second):
  """
   we will sort the splited linkedlist and then merge them back and 
   return a new linked list

  """
  new = Linkedlist()


  firsthead = first.head
  secondhead = second.head
  new.add(0)
  current = new.head
 
  while firsthead or secondhead:
   if firsthead == None:
     current.next_node = secondhead
     secondhead = secondhead.next_node
   elif secondhead == None:
      current.next_node = firsthead
      firsthead = firsthead.next_node
   else:
      if firsthead.data < secondhead.data:
        current.next_node = firsthead
        firsthead = firsthead.next_node
      else:
        current.next_node = secondhead
        secondhead = secondhead.next_node
   current = current.next_node
  head = new.head
  new_head = head.next_node
  new.head = new_head
  return new

list = Linkedlist()
list.add(10)
list.add(200)
list.add(3)
list.add(800)
list.add(1)
print(list)

result = merge_sort(list)
print(result)
   













 

