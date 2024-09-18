class Student:
    
    def __init__(self,fullname,marks):
        self.__name=fullname
        self.__marks = marks
    @staticmethod
    def welcome ():
        print("Welcome student",)
    def get_marks(self):
        print(self.__marks)
s1 = Student("Balvant",90)
s1.welcome()
# print(s1.__name)
s1.get_marks()