#q3 waf  to find the factorial of n. .
n =int(input("enter the no...."))
def calu_fact(n):
     fact=1
     for i in range(1,n+1):
        fact*=i

     print(fact)
     return fact
     
calu_fact(n)


    
    
