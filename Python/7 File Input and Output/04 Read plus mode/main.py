# r+ --> use for reading and writing but overwrites the first word means stream start from the begining
f = open("E:/1 PROGRAM DEPARTMENT/CODES/Python Code/Python [ Apna Collage ]/7 File Input and Output/04 Read plus mode/text_file.txt", "r+")
f.write("You")
print(f.read())
f.close
