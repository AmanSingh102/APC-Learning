search_number = int(input("Enter the number to be search : "))

number = (1, 4, 8, 16, 25, 36, 49, 64, 81, 100)

i = 0
while i < len(number):
    if number[i] == search_number:
        print(f"{search_number} number is found !!!!")
        break
    else:
        print(f"finding.....")
    i += 1

