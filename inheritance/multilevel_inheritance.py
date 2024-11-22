class GrandFather:
    def __init__(self, gradfathername):
        self.grandfathername = gradfathername


class Father(GrandFather):
    def __init__(self, fathername, grandfathername):
        self.fathername = fathername
        GrandFather.__init__(self, grandfathername)


class Son(Father):
    def __init__(self, sonname, fathername, grandfathername):
        self.sonname = sonname
        Father.__init__(self, fathername, grandfathername)

    def displayNames(self):
        print("Grand Father Name is = ", self.grandfathername)
        print("Father Name is = ", self.fathername)
        print("Son name is = ", self.sonname)

son = Son("Shyam","Ram","Vithal")
son.displayNames()