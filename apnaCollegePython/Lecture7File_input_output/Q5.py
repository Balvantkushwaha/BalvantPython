#From a file containing numbers separated by comma, print the count of even numbers , 
with open("apnaCollegePython\Lecture7File_input_output\digit.txt","r") as f:
    data =f.read()
    print(data)
    num = data.split(",")
    print(num)
    count =0
    for val in num:
        if(int(val)%2==0):
            count+=1
print(count)        

