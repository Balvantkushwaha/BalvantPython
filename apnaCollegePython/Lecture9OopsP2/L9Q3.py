class Person:
    name ="Balvant"
    @classmethod
    def __ChangeName__(cls,name):
       cls.name =name
       pass
       

p1 = Person()
p1.__ChangeName__("Hariom")
print(p1.name)
print(Person.name)