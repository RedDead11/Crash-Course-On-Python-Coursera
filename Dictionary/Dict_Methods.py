file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}

# for extension in file_counts:
#     print(extension) 
    
    
# for ext, amount in file_counts.items():
#     print("There are {} files with the .{} extension" .format(amount, ext))
    
print(len(file_counts))

# Values in dictionary items can be of any type

# dict = key: value 

thisDict = {
  "brand": "Ford",
  "model": "Mustang",
  "electric": False,
  "year": 1964
}

# ----------------------------- Accessing Items

# Getting value

x = thisDict["model"]
print(x)

# Getting All Values

xpp = thisDict.values()
print(xpp)

# Getting Keys

y = thisDict.keys()
print(y)

# Add a new item

thisDict["Condition"] = "Mint"

print(thisDict)


# Change Values

thisDict["year"] = 2023

print()
print(thisDict)

# Checking if key exists

if "year" in thisDict:
    print("Exists")
    
# Removing Items

thisDict.pop("year")

print()
print(thisDict)

# Updating Dictionary

thisDict.update({"year": 2023})
print()
print(thisDict)

# Removing last inserted item 

thisDict.popitem()
print()
print(thisDict)

# Clearing Dictionary
thisDict.clear()

#---------------------------  Looping

thisDict = {
  "brand": "Ford",
  "model": "Mustang",
  "electric": False,
  "year": 1964
}

# Printing Values

for x in thisDict:
    print(x)
    
# Printing Keys

for x in thisDict:
    print(thisDict[x])
