myDict = {
    "name" : "Mukest Chaursia",
    "subjects" : {
        "SSAD" : 98,
        "Python" : 99,
        "OS" : 96,
        "Statistics" : 93,
        "EVs Laws" : 97
    }
}

print("\n-------- keys Method Understanding ---------\n")
print(myDict.keys())

print("\n---- Type Casting ----")
print("List Type Casting :",list(myDict.keys()))

print("\n---- Finding total number of keys ----")
print("Number of Keys of myDict :",len(myDict))
print("\n---------------------------------------------\n")


print("\n-------- values Method Understanding ---------\n")
print("List Type Casting :",list(myDict.values()))
print("\n----------------------------------------------\n")


print("\n-------- items Method Understanding ---------\n")
print("List Type Casting :",list(myDict.items()))

# We can access individually
pairs = list(myDict.items())
print(pairs[0])
print(pairs[1])
print("\n---------------------------------------------\n")


print("\n-------- get Method Understanding ---------\n")
print(myDict["name"])       # IF NOT FOUND THEN GIVE AN ERROR
print(myDict.get("name"))   # IF NOT FOUND THEN RETURN A NONE VALUE
print("\n-------------------------------------------\n")

print("\n-------- update Method Understanding ---------\n")
myNewDict = {
    "name" : "Suresh Mehto",
    "Age" : 108
}

myDict.update(myNewDict)
print(myDict)
print("\n----------------------------------------------\n")

