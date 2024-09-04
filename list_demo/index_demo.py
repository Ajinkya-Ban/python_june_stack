lst = [] #empty list declaration
how_many_element = int(input("Enter the how many you want to insert="))
for i in range(0,how_many_element):
    lst.append(int(input("Enter the elements = ")))

print("After adding element into list")
for i in lst:
    print(i, end=" ")

which_index_gets = int(input("Enter the value = "))
print(lst.index(which_index_gets))