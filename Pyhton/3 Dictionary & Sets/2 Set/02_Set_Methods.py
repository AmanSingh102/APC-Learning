collection_set = set()

print("\n------ .add() -> Add Elemnt in Set \n")

collection_set.add(1)
collection_set.add(2)
collection_set.add(3)
collection_set.add("Aman")
collection_set.add((1,2,3,4))
print(collection_set)

print("\n------ .remove( element ) -> Remove element from a Set \n")
collection_set.remove("Aman")
print(collection_set)

print("\n------ .clear() -> Remove all element from a Set \n")
collection_set = {1, 2, 3, 4, 5}
print("Lenght :",len(collection_set))
collection_set.clear()
print("Lenght :",len(collection_set))

print("\n------ .clear() -> Remove all element from a Set \n")
collection_set = {1, 2, 3, 4, 5}
print("Remove and Print Random Value from the Set :",collection_set.pop())
print(collection_set)
print("Remove and Print Random Value from the Set :",collection_set.pop())
print(collection_set)
print("Remove and Print Random Value from the Set :",collection_set.pop())
print(collection_set)
print("Remove and Print Random Value from the Set :",collection_set.pop())
print(collection_set)
print("Remove and Print Random Value from the Set :",collection_set.pop())
print(collection_set)

print("\n------ .union() -> Give Union of Set \n")
set1 = {1, 2, 3}
set2 = {2, 3, 4}
print("Union of set1 and set2 :",set1.union(set2))
print("No Changes in Original Set :",set1)
print("No Changes in Original Set :",set2)

print("\n------ .intersection() -> Give intersection of Set \n")
set1 = {1, 2, 3}
set2 = {2, 3, 4}
print("Union of set1 and set2 :",set1.intersection(set2))
print("No Changes in Original Set :",set1)
print("No Changes in Original Set :",set2)