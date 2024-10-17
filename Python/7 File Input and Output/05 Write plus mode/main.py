# w+ --> use for reading and writing but overwrites whole
f = open("E:/1 PROGRAM DEPARTMENT/CODES/Python Code/Python [ Apna Collage ]/7 File Input and Output/05 Write plus mode/text_file.txt", "w+")
print(f.read())
f.write("You")
f.close