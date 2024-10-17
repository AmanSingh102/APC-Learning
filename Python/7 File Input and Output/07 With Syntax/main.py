# a means alias 
with open("E:/1 PROGRAM DEPARTMENT/CODES/Python Code/Python [ Apna Collage ]/7 File Input and Output/07 With Syntax/text_file.txt", "r") as f:
    data = f.read()
    print(data) 

with open("E:/1 PROGRAM DEPARTMENT/CODES/Python Code/Python [ Apna Collage ]/7 File Input and Output/07 With Syntax/text_file.txt", "w") as f:
    f.write("new data uploaded")
