#!/usr/bin/python3

def binary_search(list,target):
    """ this algorithm will outputs value of 
        element if it does exists in list
    """
    first=0
    last=len(list)-1
    

    while first <= last:

     midpoint=(first+last)//2

     if list[midpoint] == target:
         return list[midpoint]
     else:
         if list[midpoint] > target:
             last = midpoint - 1 
         else:
             first = midpoint + 1
    

    return None



def verify(value):
    if value is not None:
        print("target found and value is :",value)

    else:
        print("target not found and value is :",value)


number=[1,2,3,4,5,6,7,8,9]
binary_search(number,8)
binary_search(number,12)
result=binary_search(number,8)
result1=binary_search(number,12)
verify(result)
verify(result1)
