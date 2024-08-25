# Search for a number X in  this  tuple using loop .
num = (1,4,9,16,25,36,49,64,81,100)
x = int(input("enter the search no..."))
i=0
while(i<len(num)):
    if(num[i]==x):
        print("found of idx no.",i)
        break
    i+=1
if(i==len(num)):
    print("not found")