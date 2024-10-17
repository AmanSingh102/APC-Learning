def scratch_method_of_solving():
    with open("E:/1 PROGRAM DEPARTMENT/CODES/Python Code/Python [ Apna Collage ]/7 File Input and Output/09 Practise Set/05_print_even_number_from_file.txt", "r") as f:
        data = f.read()
        print("Numbers : ",data)

        num = ""
        for i in range(len(data)):
            if data[i] == "," :
                print(int(num))
                num = ""
            else:
                num += data[i]  

# scratch_method_of_solving()

count = 0
with open("E:/1 PROGRAM DEPARTMENT/CODES/Python Code/Python [ Apna Collage ]/7 File Input and Output/09 Practise Set/05_print_even_number_from_file.txt", "r") as f:
        data = f.read()

        numbers = data.split(",")
        print("Numbers :",numbers)

        for values in numbers:
            if int(values) % 2 == 0 :
                 count += 1

print("Total Even number :",count)