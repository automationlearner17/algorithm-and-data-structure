#!/usr/bin/python3

def shell_sort(list):
  size = len(list)
  Gap = size // 2
  value = size - 1

  while Gap > 0:
    i = 0
    gap = Gap
    while value >=  gap:
      if list[i] > list[gap]:
         removal = list[i]
         replace = list[gap]
         list[i] = replace
         list[gap] = removal
 

      i = i + 1
      print("before gap ", gap)
      gap = gap + 1
      print("after gap ",gap)
   
    
    Gap = Gap - 1


  return list


l = [0,1,89,485858558,4,10,0,799]
result = shell_sort(l)
print(result)

      


