#!/usr/bin/python3

import random

import sys

from load import load_numbers

numbers = load_numbers(sys.argv[1])
print("numbers = ", numbers)

def is_sorted(values):
   for index in range(len(values)-1):
     if values[index] > values[index+1]:
        return False
   return True

def bogo_sort(values):
    while is_sorted(values) == False:
        random.shuffle(values)
    return values   

print(bogo_sort(numbers))

