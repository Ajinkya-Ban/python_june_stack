class Mother:
    motherName = ""

    def displayMother(self):
        print(self.motherName)


class Father:
    fatherName = ""
    def displayFather(self):
        print(self.fatherName)


class Child(Mother, Father):
    def parents(self):
        print("Mother Name :", self.motherName)
        print("Father Name: ", self.fatherName)

son = Child()
son.fatherName = "Ram"
son.motherName = "Sita"
son.parents()