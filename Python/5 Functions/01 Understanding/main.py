def print_Hello_Wolrd():
    print("Namaskar Dosto...")

def add_two_numbers( num1, num2 ):
    sum = num1 + num2
    print(f"Sum of {num1} and {num2} is",sum)

def average_three_numbers( num1, num2, num3 ):
    avg = ( num1 + num2 + num3 ) / 2
    return avg

def default_parameters( a = 2, b = 3 ):
    print(f"Multiplication of {a} and {b} is {a*b}")

# -------------------------------------------------

# Greeting Function
print_Hello_Wolrd()

# Simple Function
add_two_numbers(2, 3)

# Reture Somthing
average = average_three_numbers(1, 2, 3)
print("Average =",average)

# Default Parameter Function
default_parameters()
default_parameters(2,10)
