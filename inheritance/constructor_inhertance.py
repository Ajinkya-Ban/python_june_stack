class Father:
    def __init__(self,property=0):
        self.property = property

    def display_property(self):
        print("The father has the property = ",self.property)


class Son(Father):
    def __init__(self,propert1=0,property=0):

        self.propert1 = property
        super().__init__(propert1)
    def display_property(self):
        print("The Father has the property = ", self.propert1)
        print("The son has the property = ", self.property)



son = Son(20,100)
son.display_property()