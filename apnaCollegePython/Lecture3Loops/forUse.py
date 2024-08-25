list =[1,4,9,16,25,36,49,64,81,100]
x = int(input("enter the search no...."))
idx =0
for el in list:
    if(el==x):
       print("found no. at idx",idx)
       break
    idx+=1
  