def check_for_line( word_to_check ):
    word = word_to_check
    data = True
    line_no = 1

    with open("E:/1 PROGRAM DEPARTMENT/CODES/Python Code/Python [ Apna Collage ]/7 File Input and Output/09 Practise Set/04_extract_line_found.txt", "r") as f:
        while data:
            data = f.readline()
            if word in data :
                print(f"In Line no.{line_no} exist")
                return
            line_no += 1

    return -1

check_for_line("learning")
check_for_line("programming")
