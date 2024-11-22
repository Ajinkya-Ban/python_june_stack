class Parent:
    def func1(self):
        print("I am from parent class")


class Child(Parent):
    def func1(self):
        super().func1()
        print("I am from subclass")


objChild = Child()
objChild.func1()
