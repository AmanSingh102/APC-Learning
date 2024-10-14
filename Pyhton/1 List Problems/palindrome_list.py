print("\n---------- Enter First List ------------\n")
listToCkeck = [""] * 3
for i in  range(0,3):
    listToCkeck[i] = input(f"Enter {i+1} element : ")


listReverse = listToCkeck.copy()
listReverse.reverse()

if( listToCkeck == listReverse ):
    print(f"{listToCkeck} is Palindrome")
else:
    print(f"{listToCkeck} is not Palindrome")
