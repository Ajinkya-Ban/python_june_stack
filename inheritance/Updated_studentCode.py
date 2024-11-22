from Teacher import *
class Student(Teacher):
    def setMarks(self, marks):
        self.marks = marks

    def getMarks(self):
        return self.marks

# create the object of the class
stud = Student()



stud.setId(1001)
stud.setName("Sangita")
stud.setMarks(10)

print("Id = ",stud.getId())
print("Name : ",stud.getName())
print("Marks = ",stud.getMarks())
