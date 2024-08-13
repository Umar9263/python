# Python Dictionaries

thisdict = {"brand" : "Ford", "model": "Mustang", "year": 1964}


# Dictionary
# Dictionaries are used to store data values in key:value pairs.

# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
# Dictionaries are written with curly brackets, and have keys and values:
# Dictionary items are presented in key:value pairs, and can be referred to by using the key name.


# Example
# Print the "brand" value of the dictionary:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])


# Ordered or Unordered?
# When we say that dictionaries are ordered, it means that the items have a defined order, and that order will not change.

# Unordered means that the items does not have a defined order, you cannot refer to an item by using an index.

# Changeable
# Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.



# Duplicates Not Allowed:-
# Dictionaries cannot have two items with the same key:

# Example
# Duplicate values will overwrite existing values:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020,
  "year":2001
}
print(thisdict)



#   Access Dictionary Items

# You can access the items of a dictionary by referring to its key name, inside square brackets:

# Example
# Get the value of the "model" key:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]


# There is also a method called get() that will give you the same result:

# Example
# Get the value of the "model" key:

x = thisdict.get("model")



# Add a new item to the original dictionary, and see that the keys list gets updated as well:

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

car["color"] = "white"

print(car) #after the change



# we also print  only values and add new

# Make a change in the original dictionary, and see that the values list gets updated as well:

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["year"] = 2020

print(x) #after the change



# Change Values:-

# You can change the value of a specific item by referring to its key name:

# Example
# Change the "year" to 2018:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018




# Update Dictionary:-
# The update() method will update the dictionary with the items from the given argument.

# The argument must be a dictionary, or an iterable object with key:value pairs.

# Example
# Update the "year" of the car by using the update() method:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})


# Removing Items
# There are several methods to remove items from a dictionary:


# Example:_
# The pop() method removes the item with the specified key name:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)



# Example-
# The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)



# Example:-
# The del keyword removes the item with the specified key name:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)


# Example:-
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict



# Example:-
# The clear() method empties the dictionary:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)





# Loop Dictionaries:-
# You can loop through a dictionary by using a for loop.


# ExampleGet your own Python Server
# Print all key names in the dictionary, one by one:

for x in thisdict:
  print(x)


# Example
# Print all values in the dictionary, one by one:

for x in thisdict:
  print(thisdict[x])


# Example
# You can also use the values() method to return values of a dictionary:

for x in thisdict.values():
  print(x)


# Example
# You can use the keys() method to return the keys of a dictionary:

for x in thisdict.keys():
  print(x)



# Example
# Loop through both keys and values, by using the items() method:

for x, y in thisdict.items():
  print(x, y)


# Copy a Dictionary
# You cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will only be a reference to dict1, and changes made in dict1 will automatically also be made in dict2.

# There are ways to make a copy, one way is to use the built-in Dictionary method copy().

# Example
# Make a copy of a dictionary with the copy() method:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)


# Another way to make a copy is to use the built-in function dict().

# Example:-
# Make a copy of a dictionary with the dict() function:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

mydict = dict(thisdict)
print(mydict)





# Nested Dictionaries
# A dictionary can contain dictionaries, this is called nested dictionaries.

# Example
# Create a dictionary that contain three dictionaries:

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}




# Or, if you want to add three dictionaries into a new dictionary:

# Example:-
# Create three dictionaries, then create one dictionary that will contain the other three dictionaries:

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}



# To access items from a nested dictionary, you use the name of the dictionaries, starting with the outer dictionary:

# Example
# Print the name of child 2:

print(myfamily["child2"]["name"])


# learn its method



a=[1,2,3,4,5]
b=[6,7,8,9,0]
dic={}
for i in range(len(a)):
    dic[a[i]]=b[i]

for k,v in dic.items():
    print(k,v)
print(dic[1])