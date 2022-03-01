#!/usr/bin/python3

def shell_sort(list):
  size = len(list)
  Gap = size // 2
  value = size - 1
  odd = size / 2


  if odd is int:
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
      gap = gap + 1
      
   
    
    Gap = Gap - 1
  else:
    find = 1
    while Gap >= 0 and find:
      if Gap == 0:
        find = 0
        Gap = 1
      i = 0
      gap = Gap
      while value >= gap:
        if list[i] > list[gap]:
          removal = list[i]
          replace = list[gap]
          list[i] = replace
          list[gap] = removal

        i = i + 1
        gap = gap + 1

      Gap = Gap - 1



  return list


l = [90,100,89,545454,99,0,323,1]
result = shell_sort(l)
print(result)

      


