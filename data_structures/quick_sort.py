#!/usr/bin/python3

import sys

from load import load_numbers

numbers = load_numbers(sys.argv[1])

def quick_sort(values):

  """
     we will get a pivot index from arry and then comapre the arr with pivot
     and devide the arr into two arrys the one will consists elemets which will be
     lesser than pivot and the one will be having greater than elemets and so on 
     will devide it recurresively untill we reach to single element and then we will 
     add lesser arr with pivot and greter arry and recurresively add it untllit get completed
  """

  if len(values) <= 1:
    return values
  
  lesser = []
  greater = []
  pivot = values[0]

  for value in values[1:]:
   if value < pivot:
     lesser.append(value)
   else:
     greater.append(value)
  return quick_sort(greater) + [pivot] + quick_sort(lesser)
result = quick_sort(numbers)
print(result)
