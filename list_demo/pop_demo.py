lst = [] #empty list declaration
how_many_element = int(input("Enter the how many you want to insert="))
for i in range(0,how_many_element):
    lst.append(int(input("Enter the elements = ")))

print("After adding element into list")
for i in lst:
    print(i, end=" ")
indx = int(input("\nEnter the index number = "))
remove_num =  lst.pop(indx)
print("\nThe removed element is = ",remove_num)

print("After use of pop method the element look likes,")
for i in lst:
    print(i, end=" ")