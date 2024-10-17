word = "learning"
with open("E:/1 PROGRAM DEPARTMENT/CODES/Python Code/Python [ Apna Collage ]/7 File Input and Output/09 Practise Set/03_search_word.txt", "r") as f:
    data = f.read()

    if data.find(word) != -1:   # also write if word in data :
        print("found")
    else:
        print("Not found")
