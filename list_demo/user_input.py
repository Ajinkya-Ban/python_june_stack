lst = [] #empty list declaration
how_many_element = int(input("Enter the how many you want to insert="))
for i in range(0,how_many_element):
    lst.append(int(input("Enter the elements = ")))


#insert method take the index number as well as input value from user
indx = int(input("Enter the index location = "))
value = int(input("Enter the value = "))

lst.insert(indx, value)



for i in lst:
    print(i)