# WAP to find the greatest of 4 number entered by the user . 
a = int(input("enter the first no."))
b = int(input("enter the second no."))
c = int(input("enter the third no."))
d = int(input("enter the fourth no."))

if(a>b and a>c and a>d):
    print(a," is large no.")
elif(b>a and b>c and b>d):
    print(b ," is large no.")
elif(c>a and c>b and c>d):
    print(c," is large no.")
else:
    print(d, " is large no.")
