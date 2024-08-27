#q3 .
n =int(input("enter the no...."))
def calu_fact(n):
     fact=1
     for i in range(1,n+1):
        fact*=i

     print(fact)
     return fact
     
calu_fact(n)

#q4.

def convert(usd_value):
    inr_value = usd_value*83
    print(usd_value,"USD =",inr_value,"INR")

convert(1)
    
    
