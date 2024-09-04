lst = []
how_many_elements = int(input("Enter the how many elements you want = "))
for i in range(0, how_many_elements):
    lst.append(int(input("Enter the elements = ")))

search = int(input("Enter the number to get the count = "))
if search in lst:
    print(lst.count(search))
else:
    print("Element not present")