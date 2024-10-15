def factorial( number ):
    fact = 1
    for i in range(1, number + 1):
        fact *= i
    
    print(f"Factorial of {number} is {fact}")

# -----------------------------------------------
factorial(5)
