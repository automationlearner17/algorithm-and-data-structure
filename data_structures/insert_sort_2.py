#!/usr/bin/python3

"""
    In this algorithm we will itrriate the unsorted list's element with its the same list element in 
    order to get a sorted list , We will first start our comparision of list from first element
    and we start assuming that element as sorted one then we start going forward and will comapare 
    with next one and will compare and do for thrid one and compare for first and second and so on 
    for Nth element of list will compare for N-1 its behind elements and finally the list will be 
    sorted so the time complexity of this algorithm is sqaure of N.

"""

def insert_sort(list):
   for i in range(1,len(list)):
       value = list[i]
       j = 0
       while j < i:
          if list[j] > value:
            replace = list.pop(i)
            list.insert(j,replace) 
            j = i
          j = j + 1

   return list


l = [100,6,7887,3977,4677,0,10]

result = insert_sort(l)
print(result) 
             
         
          
         
