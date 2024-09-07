def check_for_world(word):
    
  with open("apnaCollegePython\Lecture7File_input_output\pratice.txt", "r") as f:
       data = f.read()
       if(data.find(word)!=-1):
              print("found")
       else:
              print("not found")    
check_for_world("learning" )