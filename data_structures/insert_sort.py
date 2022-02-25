#!/usr/bin/python3

def insert_sort(list):
  """
    we start adding elements from unsorted list one by one to a new list 
    with sorting it for all elements and that will be returned as a sorted
    new list
  """

  new = []

  for i in range(0,len(list)):
     value = list[i]
     length = len(new)
     if length < 1:
       new.insert(0,value)
     else:
       minimum = None
       index = 0
   
       while minimum == None and length > index:
          if new[index] > value:
             minimum = index
          index = index + 1
   
             
       if minimum == None:
          new.append(value)
       else:
          new.insert(minimum,value)

  return new



l = [100,600,60,6000000,7,8,40,3000000]

result = insert_sort(l)
print(result)
         
