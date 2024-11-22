def sayHello():
    print("Good morning")
    n1 = 30
    n2 = 40
    print(n1 + n2)


def sayBye():
    print("Good bye...")


def doAdd(x, y):
    result_add = x + y
    return result_add


def doMultiplications(n1, n2):
    doAdd(n1, n2)
    result_mul = n1 * n2
    # result_add = n1 + n2
    return result_mul, doAdd(n1, n2)


def personalInfo(name, mob=9877667677):
    print("The name is = ", name)
    print("The contact number is = ", mob)


def Adder(*num):
    sum = 0
    for i in num:
        sum = sum + i
    print("The sum is = ",sum)


def personalData(**data):
    for key,value in data.items():
        print("{} is {}".format(key,value))
