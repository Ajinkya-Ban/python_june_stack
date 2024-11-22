num = 5
str1 = "hello"
try:
    result = num + str1
    print(result)
except TypeError as err:
    print(err)

print("hello")