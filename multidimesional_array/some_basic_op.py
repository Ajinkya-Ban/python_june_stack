import numpy
from numpy import *

arr1 = array(
    [
        [1,2],
        [3,4]
    ]
)
arr2 = array(
    [
        [5,6],
        [7,8]
    ]
)

# rows = concatenate((arr1,arr2),axis=0)
# print(rows)
#
# cols = concatenate((arr1,arr2),axis=1)
# print(cols)

#to print specific rows data as well as specific cols data

element = arr1[1,1]
print(element)

# we can also use the slicing
element1 = arr1[:2,:]
print(element1)

#arithmatic operations, addition, subtraction, multiplication, divide, mod
arr3 = arr1 + arr2
print("The result is = ",arr3)

# we can also use the aggrigate functions
result = sum(arr2)
print("The sum result is =", result)

result2 =  mean(arr2)
print("The mean is = ",result2)

result3 =  median(arr2)
print("The median is = ",result3)
