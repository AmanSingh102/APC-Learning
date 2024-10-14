number = int(input("Enter the number : "))
sum = 0

i = 1
while i <= number:
    sum = sum + i
    i += 1

print(f"Sum of {number} natural number is {sum}")