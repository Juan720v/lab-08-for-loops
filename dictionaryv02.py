myData = {"effective top tube length": 515, "seat tube length": 500, "seat tube angle": 74.4, "head tube angle": 70.5, "stack": 513, "reach": 367, "standover height": 755}

myKeys = [] # this is an empty array or list
myValues = []

# parellel iteration

for k, v in myData.items():
    # k is all the orange things in the first line
    # v is the keys
    # .items is a method that allows us to iterate as many items as there are "items" inside our dictionary
    print("key: " + str(k) + ", value: " + str(v))

myKeys = list(myData.keys())
myValues = list(myData.values())

print("ALL KEYS: " + str(myKeys))
print("ALL VALUES: " + str(myValues))