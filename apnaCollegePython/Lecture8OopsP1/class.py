class Student:
    college_name = "MCBU"
    name = "No name "
    marks =  0
    #default constructors 
    def __init__(self):
        pass
    #parameterized constructors
    def __init__(self , name,marks):
        self.name = name
        self.marks = marks
        print("add new student in database ")
s1 = Student("balvant kushwaha" , 80)
print(s1.name,s1.marks ,s1.college_name)
s2 = Student("hariom",90)
print(s2.name,s1.marks)
s3  = Student("",89)
print(s3.name,s3.marks,s3.college_name)