#!/usr/bin/python3

def merge_sort(list):
 """ 
    In this algorithm we will use devide and conquer method and then merge the devided sorted lists recurresivily using following steps
     1. devide the list in sub lists
     2. sort the sublists recurrsively 
     3. merge the sorted sublists 
 """
 if len(list) <= 1:
   return list
   
 first_half, second_half = split(list)
 first = merge_sort(first_half)
 second = merge_sort(second_half)

 return merge(first,second)


def split(list):
   """ 
      This function will split the list into two sublist from mid point 
      returns two new lists

   """ 
   mid = (len(list))//2
   first_half = list[:mid]
   second_half = list[mid:]

   return first_half,second_half

def merge(first,second):
   """
     This function will sort two list and then append those sorted values into new list
     return new sorted list
   """
   l = []
   i = 0
   j = 0
   
   while i < len(first) and j < len(second):
     if first[i] < second[j]:
       l.append(second[j])
       j = j + 1
     else:
       l.append(first[i])
       i = i + 1

   while i < len(first):
      l.append(first[i])
      i = i + 1
   while j < len(second):
      l.append(second[j])
      j = j + 1
   
   return l

def verify(list):
   n = len(list)
   if n == 0 or n == 1:
     return True

   return list[0] > list[1] and verify(list[1:])

alist = [200,10,40,70,500,700,800,4,600,3,2,1000]
result = merge_sort(alist)
verify(result)
#print(result)
ver = verify(result)

def cross(verify):
 if verify == True:
   print("we are done")
 else:
   print("there is problem")
cross(ver)


 
