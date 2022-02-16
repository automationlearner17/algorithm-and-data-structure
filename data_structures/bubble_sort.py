#!/usr/bin/python3

def bubble_sort(list):
  """
    in bubble sort we use to ittirate the list's elements from every index with its consicutive index element and if it is greater
    the consicutive one than we swipe the element with the consucutive one and if it is not then we skip and do the same process
    with next two elements and we do this for number of times this list contains elements for and the time complexity will be 
    square of n as we will ittriate the every element of list for numbers of time the list contains elements
  """


  for i in range(0,len(list)):
     list = swiping(list)
  return list
     
def swiping(list):
  for i in range(0,len(list)-1):
    if list[i] > list[i+1]:
      swipe = list[i]
      new = list[i+1]
      list[i+1] = swipe
      list[i] = new
  return list

l = [1000,6,7,4,50000,299,600]
result = bubble_sort(l)

print(result)
    
      
