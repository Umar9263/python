#Python Tuples

mytuple = ("apple", "banana", "cherry")

# A tuple is a collection which is ordered and unchangeable.
# Tuples are written with round brackets.

# Tuple Items:-
# Tuple items are ordered, unchangeable, and allow duplicate values.
# Tuple items are indexed, the first item has index [0]

# Ordered:-
# When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.

# Unchangeable:-
# Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.


# Allow Duplicates
# Since tuples are indexed, they can have items with the same value:

# Example

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)






# Access Tuple Items
# You can access tuple items by referring to the index number, inside square brackets:

# Example
# Print the second item in the tuple:

thistuple = ("apple", "banana", "cherry")
print(thistuple[1])



# Negative Indexing
# Negative indexing means start from the end.

# -1 refers to the last item, -2 refers to the second last item etc.

# Example
# Print the last item of the tuple:

thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])



# Range of Indexes
# You can specify a range of indexes by specifying where to start and where to end the range.

# When specifying a range, the return value will be a new tuple with the specified items.

# Example
# Return the third, fourth, and fifth item:

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])




# Range of Negative Indexes
# Specify negative indexes if you want to start the search from the end of the tuple:

# Example
# This example returns the items from index -4 (included) to index -1 (excluded)

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])



# Check if Item Exists
# To determine if a specified item is present in a tuple use the in keyword:

# Example
# Check if "apple" is present in the tuple:

thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")



#   Update Tuples

# Change Tuple Values
# Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.

# But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.

# Example
# Convert the tuple into a list to be able to change it:

x = ("apple", "banana", "cherry")
y = list(x)

y[1] = "kiwi"
x = tuple(y)
 
print(x)


# 2. Add tuple to a tuple. You are allowed to add tuples to tuples, so if you want to add one item, (or many), create a new tuple with the item(s), and add it to the existing tuple:

# Example
# Create a new tuple with the value "orange", and add that tuple:

thistuple = ("apple", "banana", "cherry")
y = ("orange")
thistuple += y

print(thistuple)




# Remove Items:-

# Tuples are unchangeable, so you cannot remove items from it, but you can use the same workaround as we used for changing and adding tuple items:

# Example
# Convert the tuple into a list, remove "apple", and convert it back into a tuple:

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)




# Or you can delete the tuple completely:

# Example
# The del keyword can delete the tuple completely:

thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists



# Unpack Tuples:-

# When we create a tuple, we normally assign values to it. This is called "packing" a tuple:
# Packing a tuple:

# fruits = ("apple", "banana", "cherry")


# But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking":

# Example
# Unpacking a tuple:

fruits = ("apple", "banana", "cherry")

a, b, c = fruits

print(a)
print(b)
print(c)


# Using Asterisk*
# If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list:

# Example
# Assign the rest of the values as a list called "red":

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)



# Loop Tuples:-

# You can loop through the tuple items by using a for loop.

# Example
# Iterate through the items and print the values:

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)


# Using a While Loop
# You can loop through the tuple items by using a while loop.

# Use the len() function to determine the length of the tuple, then start at 0 and loop your way through the tuple items by referring to their indexes.

# Remember to increase the index by 1 after each iteration.

# Example
# Print all items, using a while loop to go through all the index numbers:

thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1


# Join Tuples:-

# To join two or more tuples you can use the + operator:

# ExampleGet your own Python Server
# Join two tuples:

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)



# Multiply Tuples
# If you want to multiply the content of a tuple a given number of times, you can use the * operator:

# Example
# Multiply the fruits tuple by 2:

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)

# now lear about its method