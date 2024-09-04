lst1 = []
lst2 = []
how_many_elements = int(input("Enter the how many elements you want = "))
for i in range(0, how_many_elements):
    lst1.append(int(input("Enter the elements = ")))

lst2 = lst1.copy()
print(lst2)