from array import *
arr = array('i',[])

how_many_element = int(input("Enter how many element you want = "))

for i in range(0,how_many_element):
    arr.append(int(input("Enter the elements = ")))


for i in arr:
    print(i, end=" ")