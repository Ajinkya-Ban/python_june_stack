class BookX:
    def __init__(self,pages):
        self.pages = pages

    def __add__(self, other):
        return self.pages + other.pages
class BookY:
    def __init__(self,pages):
        self.pages = pages
x = BookX(100)
y = BookY(200)
print("Total pages = ",x+y)
