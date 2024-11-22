import numpy
from numpy import *

rows1 = int(input("Enter the number of rows for array1 = "))
cols1 = int(input("Enter the number of cols for array1 = "))

rows2 = int(input("Enter the number of rows for array2 = "))
cols2 = int(input("Enter the number of cols for array2 = "))

print(f"\nEnter the element for array1 ({rows1} X {cols1})")
array1 = []
for i in range(rows1):
    row = list(map(int,input(f"Row {i + 1}= ").split()))
    array1.append(row)
res_arr1 = array(array1)

print(f"\nEnter the element for array2 ({rows2} X {cols2})")
array2 = []
for i in range(rows2):
    row = list(map(int,input(f"Row= {i + 1}= ").split()))
    array2.append(row)
res_arr2 = array(array2)

#choose the operation
print("Select your choice")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")

choice = int(input("Enter your choice number = "))
match(choice):
    case 1:
        if numpy.shape(res_arr1) == numpy.shape(res_arr2):
            print("The addition is")
            print(res_arr1 + res_arr2)
        else:
            print("Invalid dimensions")

    case 2:
        if numpy.shape(res_arr1) == numpy.shape(res_arr2):
            print("The subtraction is")
            print(res_arr1 - res_arr2)
        else:
            print("Invalid dimensions")

    case '_':
        print("Invalid choice")