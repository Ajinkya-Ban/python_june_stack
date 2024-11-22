import numpy
from numpy import *
from numpy.ma import ndim

# arr = array([1,2,3,4])
# arr = arr * 5
# print(arr)

# arr1 = array([5,6,7,8])
# arr2 = array([1,2,3,4])
#
# arr3 = arr1 - arr2
# print(arr3)

# arr1 = array([5,6,7,8])
# print(numpy.sin(arr1))
# print(max(arr1))
# print(sum(arr1))

arr1 = array([[4,6,7,9],[5,6,7,8]])
arr2 = array([1,10,3,44,55])

print("The ndim = ",ndim(arr1))
print("The size() = ", size(arr2))
print("The shape() = ", shape(arr1))
print("The itemsize() = ",arr2.itemsize)
print("nbyte() = ",arr2.nbytes)

arr3 = arr1.reshape(4,2)
print(arr3)


# result = arr1 > arr2
# print(result)
# print("Any result = ",any(result))
# print("all result = ",all(result))

