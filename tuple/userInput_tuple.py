# First we declare empty list
lst = []

#set the limit that how many element you want to insert

how_many_element = int(input("Enter how many elements = "))

for i in range(0, how_many_element):
    #take the user input upto how_many_elements
    lst.append(int(input(f"Enter the element of {i+1} = ")))

tup = tuple(lst) # here we can convert the list into tuple using the inbuilt function tuple().
print(type(tup)) # here we can check the type of tuple.

for i in tup:
    print(i)

