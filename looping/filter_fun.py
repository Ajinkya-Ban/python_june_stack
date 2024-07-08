from functools import *

# def even_num(x):
#     if x % 2==0:
#         return True
#     else:
#         return False
#
# lst = [2,3,4,5,7,8,9]
#
# filters = list(filter(even_num,lst))
# print(filters)

# def even_num(x):
#    return  x * x
#
# lst = [2,3,4,5,7,8,9]
#
# filters = list(map(even_num,lst))
# print(filters)

# lst = [1,2,3,4,8,9,7]
# result = reduce(lambda x,y:x*y,lst)
# print(result)

def sequre(x):
    return lambda x:x*x

res = sequre(5)
print(res)