#!/usr/bin/python3

def linear_search(list,target):
    """ this algorithm is used to get an index value of list
        if it ddoes exists
    """
    for i in range(0,len(list)):
        if list[i]==target:
            return i
    
    return None

def verify(index):
    if index is not None:
        print("target found: ", index)
       
    else:
        print("target not found")

number = [1,2,3,4,5,6,7,8,9,10]
linear_search(number,12)
linear_search(number,6)

result=linear_search(number,12)
result1=linear_search(number,6)
verify(result)
verify(result1)
