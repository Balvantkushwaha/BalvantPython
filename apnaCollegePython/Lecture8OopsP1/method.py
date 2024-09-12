class Student:
    def __init__(self,fullname,marks):
        self.name=fullname
        self.marks = marks
    @staticmethod
    def welcome ():
        print("Welcome student",)
    def get_marks(self):
        return self.marks
s1 = Student("Balvant",90)
print(s1.welcome())
print(s1.get_marks())