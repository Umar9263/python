# Python Set

myset = {"apple", "banana", "cherry"}


# Set:-

# Sets are used to store multiple items in a single variable.
# A set is a collection which is unordered, unchangeable*, and unindexed.



# Sets are written with curly brackets.

# Example
# Create a Set:

thisset = {"apple",True,"banana",1, "banana",0,False, "cherry"}
print(thisset)

# Set items are unordered, unchangeable, and do not allow duplicate values.

# Sets cannot have two items with the same value.




# Access Set Items:-

# You cannot access items in a set by referring to an index or a key.

# But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.


# Example
# Check if "banana" is present in the set:

thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)


# add item:-

# To add one item to a set use the add() method.

# Example
# Add an item to a set, using the add() method:

thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)



# Add Sets:-
# To add items from another set into the current set, use the update() method.

# Example
# Add elements from tropical into thisset:

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)



# Add Any Iterable:-
# The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).

# Example
# Add elements of a list to at set:

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)



# Remove Item:-
# To remove an item in a set, use the remove(), or the discard() method.

# Example
# Remove "banana" by using the remove() method:

thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)


# Example:-
# Remove "banana" by using the discard() method:

thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)



# Loop Items:-
# You can loop through the set items by using a for loop:

# Example
# Loop through the set, and print the values:

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)





#   Join Two Sets:-
# There are several ways to join two or more sets in Python.

# You can use the union() method that returns a new set containing all items from both sets, or the update() method that inserts all the items from one set into another:

# Example
# The union() method returns a new set with all items from both sets:

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)


# Example
# The update() method inserts the items in set2 into set1:

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)


# learn set other mathod