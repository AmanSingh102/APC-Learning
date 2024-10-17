print("\n ---- Printing a whole line ---- ")
f = open("E:/1 PROGRAM DEPARTMENT/CODES/Python Code/Python [ Apna Collage ]/7 File Input and Output/01 Underdstanding/01_Text_File.txt","r")
data = f.read()

print(data)
print(type(data))

f.close()

# ------------------------------------------------------------------------------------------------------------------------------------------------------------

print("\n ---- Printing a certain line ---- ")
f = open("E:/1 PROGRAM DEPARTMENT/CODES/Python Code/Python [ Apna Collage ]/7 File Input and Output/01 Underdstanding/01_Text_File.txt","r")

data = f.read(5)
print(data)

f.close()

# ------------------------------------------------------------------------------------------------------------------------------------------------------------

print("\n ---- Printing one line at a line ---- ")
f = open("E:/1 PROGRAM DEPARTMENT/CODES/Python Code/Python [ Apna Collage ]/7 File Input and Output/01 Underdstanding/01_Text_File.txt","r")

line1 = f.readline() 
print(line1, end="")
line1 = f.readline() 
print(line1)

f.close()

# ------------------------------------------------------------------------------------------------------------------------------------------------------------

print("\n ---- Above logic and other understanding ---- ")
f = open("E:/1 PROGRAM DEPARTMENT/CODES/Python Code/Python [ Apna Collage ]/7 File Input and Output/01 Underdstanding/01_Text_File.txt","r")

data = f.read()
print(data)         # This print the whole line and pointer shifted the last so there is nothing left to read

line1 = f.readline() 
print(line1)
line2 = f.readline() 
print(line2)

f.close()