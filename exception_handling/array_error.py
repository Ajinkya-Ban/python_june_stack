lst = [1,2,3]
try:
    print(lst[1])
    print(lst[3])
except IndexError as e:
    print(e)
print("welcome to python")