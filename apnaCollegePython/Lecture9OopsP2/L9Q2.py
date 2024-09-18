class Car:
    def __init__(self,type):
        self.type = type
    @staticmethod
    def start():
        print("start car ...")
    @staticmethod
    def stop():
        print("car stop...")
class ToyotoCar(Car):
    def __init__(self , name , type):
        super().stop
        self.name =name
        self.type =type 

car1 = Car("prius")
car2 = ToyotoCar("prius","eletric")
car2.start()
car1.stop()