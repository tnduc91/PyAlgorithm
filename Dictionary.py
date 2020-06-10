dict = {
    1: "one",
    2: "two",
    3: "three"
}

dict[4] = "four"
del dict[4]

print (dict)
print (dict[1])
print (dict.get(1))

for key in dict:
    print ("key = {}, value = {}".format(key, dict[key]))

for key, val in dict.items():
    print (key, val)


# Copy a dictionary
dict2 = dict.copy()