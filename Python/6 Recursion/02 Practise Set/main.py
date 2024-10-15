# Sum of Natural Number using Recursion
def sum_of_natural_numbers( number ):
    if number == 0:
        return 0
    return sum_of_natural_numbers( number - 1 ) + number 

# Printing all the elements of list using Recursion
def print_element_of_list( list, index = 0 ):
    if index == len(list):
        return
    print(list[index], end=", ")
    print_element_of_list(list, index + 1)

# -----------------------------------------------------------
print("Sum of 5 Natural Number :",end=" ")
print(sum_of_natural_numbers(5))

# -----------------------------------------------------------
animals = ["Lion", "Monkey", "Donkey", "Goat"]
print(f"\nList of Animals :", end=" ")
print_element_of_list(animals)
print("\n")