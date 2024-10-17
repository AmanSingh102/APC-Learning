# w ---> overwrites the entire file

f = open("E:/1 PROGRAM DEPARTMENT/CODES/Python Code/Python [ Apna Collage ]/7 File Input and Output/02 Write mode/text_file.txt", "w")

text = input("Enter the text you want to overwrite [ Caution all the previous data will be erased ] : ")
f.write(text)
print("File successfully overwrite.......")

f.close()