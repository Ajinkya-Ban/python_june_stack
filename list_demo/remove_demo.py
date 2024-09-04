lst = [] #empty list declaration
how_many_element = int(input("Enter the how many you want to insert="))
for i in range(0,how_many_element):
    lst.append(int(input("Enter the elements = ")))

print("After adding element into list")
for i in lst:
    print(i, end=" ")

which_value_remove = int(input("\nEnter the value to be removed = "))
if which_value_remove in lst:
    lst.remove(which_value_remove)

    print("\nAfter remove the list look like,")
    for i in lst:
        print(i, end=" ")
else:
    print("Please check the value, value not found")

