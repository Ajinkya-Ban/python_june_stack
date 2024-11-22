class Addition:
    firstNumber = 20
    secondNumber = 30

    def doAdd(self):
        print("The addition is = ",self.firstNumber + self.secondNumber)

    def doSub(self):
        print("The subtraction is = ", self.firstNumber - self.secondNumber)

add = Addition()
add1 = Addition()
add.doAdd()
add1.doSub()