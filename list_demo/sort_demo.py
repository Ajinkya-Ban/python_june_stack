lst = [] #empty list declaration
how_many_element = int(input("Enter the how many you want to insert="))
for i in range(0,how_many_element):
    lst.append(int(input("Enter the elements = ")))

print("After adding element into list")
for i in lst:
    print(i, end=" ")

lst.sort(reverse=False)

print("\nAfter sorting the element are")
for i in lst:
    print(i, end=" ")