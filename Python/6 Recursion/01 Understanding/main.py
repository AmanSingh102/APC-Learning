# Recursive Function
def print_natural_number( n ):
    if n == 0:
        return
    print(n, end=" ")
    print_natural_number( n - 1 )

# ---------------------------------
print("Number :", end=" ")
print_natural_number(5)


# Factorial using Recusion
def factorial( n ):
    if n == 0 or n == 1 :
        return 1
    else :
        return n * factorial( n - 1 )
    
# ----------------------------------
print("\n\nFactoral of 5 :", end=" ")
print(factorial(5))


# Fibonacci using Recursion
def fibonacci( n ):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci( n - 1 ) + fibonacci( n -2 )

# ------------------------------------------------------
print("\nFibonacci of 6 :",end=" ")
print(fibonacci(6))