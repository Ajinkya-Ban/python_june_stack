class square(object):
    def __init__(self, x):
        self.x = x

    def area(self):
        print("The square is = ", self.x * self.x)


class Rectangle(square):
    def __init__(self, x, y):
        super().__init__(x)
        self.y = y

    def area(self):
        super().area()
        print("The area of rectangle is = ", self.x * self.y)


n1, n2 = [float(x) for x in input("Enetr the two values by space seprated = ").split()]
rect = Rectangle(n1, n2)
rect.area()
