info = {
    "key" : "value",
    "name" : "Mukesh",
    "Language" : "Mogolia",
    "Age" : 19,
    "Height" : 5.7,
    "IsAdult" : True,

    # We can also stored list and tuples
    "subjects" : ["SSD", "Python", "Statistics", "EVs Laws", "OS"],
    "pythonTopics" : ("List", "Tuple", "Dictionary", "Sets")

    # don't allow duplicate key
}

print()
print(info)
print()
print(type(info))

print("\n---- We can access individual ----")
print(info["name"])
print(info["Age"])
print(info["Language"])
print(info["IsAdult"])
print(info["Height"])

print("\n---- We can also assign the same key ----")
info["name"] = "Raju"
print(info["name"])

print()

null_Dict = {}
print(null_Dict)