# w ---> overwrites the entire file

f = open("E:/1 PROGRAM DEPARTMENT/CODES/Python Code/Python [ Apna Collage ]/7 File Input and Output/03 Append mode and Read Function/text_file.txt", "a")

text = input("Enter the text you want to append : ")
f.write(text)
print("File successfully appended.......")

f.close()