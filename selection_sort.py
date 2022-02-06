#!/usr/bin/python3
import sys
from load import load_numbers

numbers = load_numbers(sys.argv[1])

def selection_sort(values):
  new_sort = []
  print("%-25s %-25s" % (values,new_sort))

  for index in range(len(values)):
    min_to_move = min_move(values)
    new_sort.append(values.pop(min_to_move))
    print("%-25s %-25s" % (values,new_sort))
  return new_sort

def min_move(values):
  min_index = 0 
  for i in range(1,len(values)):
   if values[i] < values[min_index]:
     min_index = i
  return min_index

print(selection_sort(numbers))
