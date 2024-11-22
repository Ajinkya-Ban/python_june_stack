class Addition:
    #here we can define the constructor
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2

    def doAdd(self):
        print("The addition is = ", self.num1 + self.num2)

# create the object of the class
num1 = int(input("Enter the first number = "))
num2 = int(input("Enter the second number ="))
add = Addition(num1,num2)
add.doAdd()