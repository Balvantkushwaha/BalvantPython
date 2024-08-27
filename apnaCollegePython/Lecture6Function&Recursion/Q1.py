def calu_sum(n):
    if(n==1):
     return 1
    sum = n+calu_sum(n-1)
    return sum
print(calu_sum(10))