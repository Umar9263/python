# Python Lists
mylist = ["apple", "banana", "cherry"]

                          # List
# Lists are used to store multiple items in a single variable.
# Lists are created using square brackets:

# Example:-

thislist = ["apple","banana", "banana", "cherry"]
print(thislist)


# List Items:-
# List items are ordered, changeable, and allow duplicate values.
# List items are indexed, the first item has index [0], the second item has index [1] etc.


# Ordered:-
# When we say that lists are ordered, it means that the items have a defined order, and that order will not change.
# If you add new items to a list, the new items will be placed at the end of the list.
# NOTE: There are some list methods that will change the order, but in general: the order of the items will not change.


# Changeable:-
# The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.



# Allow Duplicates:-
# Since lists are indexed, lists can have items with the same value:
# Example
# Lists allow duplicate values:

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)



# List Items - Data Types:-
# List items can be of any data type:
# Example
# String, int and boolean data types:

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]



# The list() Constructor:--
# It is also possible to use the list() constructor when creating a new list.
# Example
# Using the list() constructor to make a List:

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)
print(type(thislist))



############################################################################################################
############################################################################################################

                            # Access List Item
# List items are indexed and you can access them by referring to the index number:
# Example:-
# Print the second item of the list:

thislist = ["apple", "banana", "cherry"]
print(thislist[1])           





# Negative Indexing:-
# Negative indexing means start from the end

# -1 refers to the last item, -2 refers to the second last item etc.

# Example:-
# Print the last item of the list:

thislist = ["apple", "banana", "cherry"]
print(thislist[-1])



# Range of Indexes
# You can specify a range of indexes by specifying where to start and where to end the range.
# When specifying a range, the return value will be a new list with the specified items.


# Example:-
# Return the third, fourth, and fifth item:

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])



# By leaving out the start value, the range will start at the first item:-
# Example
# This example returns the items from the beginning to, but NOT including, "kiwi":

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])




# By leaving out the end value, the range will go on to the end of the list:-
# Example
# This example returns the items from "cherry" to the end:

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])




# Range of Negative Indexes:-
# Specify negative indexes if you want to start the search from the end of the list:

# Example
# This example returns the items from "orange" (-4) to, but NOT including "mango" (-1):

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])




# Check if Item Exists:-
# To determine if a specified item is present in a list use the in keyword:

# Example
# Check if "apple" is present in the list:

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes")




############################################################################################################
############################################################################################################
                              # Change List Items:-

# Change Item Value:-
# To change the value of a specific item, refer to the index number:

# Example
# Change the second item:

thislist = ["apple", "banana", "cherry"]
thislist[1] = "mango"
print(thislist)





# Change a Range of Item Values
# To change the value of items within a specific range, define a list with the new values, and refer to the range of index numbers where you want to insert the new values:

# Example
# Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon":

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:4] = ["blackcurrant","a"]
print(thislist)






# Insert Items:-
# To insert a new list item, without replacing any of the existing values, we can use the insert() method.

# The insert() method inserts an item at the specified index:

# Example
# Insert "watermelon" as the third item:

thislist = ["apple", "banana", "cherry"]
thislist.insert(1,"mango")
print(thislist)



############################################################################################################
############################################################################################################

                              #Add List Items


# Append Items:-
# To add an item to the end of the list, use the append() method:

# Example
# Using the append() method to append an item:

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

# Extend List
# To append elements from another list to the current list, use the extend() method.

# Example
# Add the elements of tropical to thislist:

list1 = ["apple", "banana", "cherry"]
list2 = ["mango", "pineapple", "papaya"]
list1.extend(list2)
print(list1)


# Add Any Iterable:-
# The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).

# Example
# Add elements of a tuple to a list:

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)


############################################################################################################
############################################################################################################

                              # Remove List Items:-

# Remove Specified Item
# The remove() method removes the specified item.

# Example
# Remove "banana":

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)




# Remove Specified Index
# The pop() method removes the specified index.

# Example
# Remove the second item:

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)




# The del keyword also removes the specified index:

# Example
# Remove the first item:

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)





# The del keyword can also delete the list completely.

# Example
# Delete the entire list:

this = ["apple", "banana", "cherry"]
del this
print(this)





# Clear the List
# The clear() method empties the list.

# The list still remains, but it has no content.

# Example
# Clear the list content:

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)





############################################################################################################
############################################################################################################

                                #Loop Lists

# Loop Through a List:-
#   You can loop through the list items by using a for loop:-

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)





# Using a While Loop:-
# You can loop through the list items by using a while loop.

# Use the len() function to determine the length of the list, then start at 0 and loop your way through the list items by referring to their indexes.

# Remember to increase the index by 1 after each iteration.

# Example:-
# Print all items, using a while loop to go through all the index numbers:-

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1




  
############################################################################################################
############################################################################################################
                      #List Comprehension

# List Comprehension:-
# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

# Example:

# Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.

# Without list comprehension you will have to write a for statement with a conditional test inside:


# Example:-
fruits = ["apple", "banana", "acherry", "kiwi", "amango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)



###########################################################################################################
###########################################################################################################

                                #Sort Lists

# Sort List Alphanumerically:-
# List objects have a sort() method that will sort the list alphanumerically, ascending, by default:

# ExampleGet your own Python Server
# Sort the list alphabetically:

thislist = ["arange", "dango", "eiwi", "cineapple", "banana"]
thislist.sort()
print(thislist)


# Example
# Sort the list numerically:

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)



# Sort Descending
# To sort descending, use the keyword argument reverse = True:

# Example
# Sort the list descending:

thislist = ["orange", "mango", "kiwi", "z","pineapple", "banana","apple"]
thislist.sort(reverse = True)
print(thislist)
 

# Example
# Sort the list descending:

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)


# Reverse Order
# What if you want to reverse the order of a list, regardless of the alphabet?

# The reverse() method reverses the current sorting order of the elements.

# Example
# Reverse the order of the list items:

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)


##########################################################################################################
##########################################################################################################

                          #Copy Lists

# You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.

# There are ways to make a copy, one way is to use the built-in List method copy().

# ExampleGet your own Python Server
# Make a copy of a list with the copy() method:

list1 = ["apple", "banana", "cherry"]
list2 = list1.copy()
print(list2)




# Another way to make a copy is to use the built-in method list().

# Example
# Make a copy of a list with the list() method:

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)




##########################################################################################################
##########################################################################################################

                              #Join Lists

# Join Two Lists
# There are several ways to join, or concatenate, two or more lists in Python.

# One of the easiest ways are by using the + operator.

# ExampleGet your own Python Server
# Join two list:

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)





# Another way to join two lists is by appending all the items from list2 into list1, one by one:

# Example
# Append list2 into list1:

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)




# Or you can use the extend() method, which purpose is to add elements from one list to another list:

# Example
# Use the extend() method to add list2 at the end of list1:

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)


# now learn about list method