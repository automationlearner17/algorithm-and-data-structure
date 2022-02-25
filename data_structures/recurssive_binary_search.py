#!/usr/bin/python3

def resurrsive_binaray_search(list,target):
    """ this algorithm is going to work as binary search
        but with differnet way and will return value of 
        element if it does exists in list
    """

    if len(list) > 0:
        midpoint = (len(list))//2

        if list[midpoint] == target:
            return list[midpoint]
        else:
            if list[midpoint] > target:
                
              return resurrsive_binaray_search(list[:midpoint-1],target)
            else: 
               return  resurrsive_binaray_search(list[midpoint+1:],target)

        
        return None


def verify(value):
    if value is not None:
        print("value is there :",value)

    else:
        print("value is not there")


number =[1,2,3,4,5,6,7,8,9]
resurrsive_binaray_search(number,8)
resurrsive_binaray_search(number,12)

result = resurrsive_binaray_search(number,8)
result1 = resurrsive_binaray_search(number,12)

verify(result)
verify(result1)

