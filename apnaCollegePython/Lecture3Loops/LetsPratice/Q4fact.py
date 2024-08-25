# wap to find the factorial of first n numbers (using for)
n = int(input("enter the no....\n  "))
fact =1
for i in range(1,n+1):
    fact*=i
print(fact)