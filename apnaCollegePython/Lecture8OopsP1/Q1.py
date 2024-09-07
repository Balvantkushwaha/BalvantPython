class Studnet:
    def __init__(self,name,marks):
        self.name =name
        self.marks =marks
    def get_avg(self):
        sum= 0
        for var in self.marks:
            sum+=var 
        print("hii",self.name,"Your avg score is :" ,sum/6)
s1 = Studnet("Abhishek ",[99,97,92,90,89,79])
s1.get_avg()
        
        
