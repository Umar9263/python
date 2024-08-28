# Python Strings

# Strings in python are surrounded by either single quotation marks, or double quotation marks.
# 'hello' is the same as "hello".

# You can display a string literal with the print() function:
# Example:-
print("Hello")
print('Hello')

#-------------------------------------


# Assign String to a Variable
# Assigning a string to a variable is done with the variable name followed by an equal sign and the string:

# Example
a = "Hello"
print(a)

#-------------------------------------

            # Multiline Strings
# You can assign a multiline string to a variable by using three quotes:
# Example:-
# You can use three double quotes:

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)


# Or three single quotes:

# Example
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''

print(a)

#-------------------------------------


                    # Strings are Arrays:-
# Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.
# However, Python does not have a character data type, a single character is simply a string with a length of 1.
# Square brackets can be used to access elements of the string.

# Example
# Get the character at position 1 (remember that the first character has the position 0):

a = "Hello, World!"
print(a[1])

#-------------------------------------

            # Looping Through a String:-
# Since strings are arrays, we can loop through the characters in a string, with a for loop.
# Example
# Loop through the letters in the word "banana":

for x in "banana":
  print(x)

#-------------------------------------

            # String Length:-
# To get the length of a string, use the len() function.
# Example
# The len() function returns the length of a string:

a = "Hello, World!"
print(len(a))

#-------------------------------------

            # Check String
# To check if a certain phrase or character is present in a string, we can use the keyword in.
# Example
# Check if "free" is present in the following text:

txt = "The best things in life are free!"
print("free" in txt)

#-------------------------------------

            # Use it in an if statement:
# Example
# Print only if "free" is pre

txt = "The best things in life are free!"
if "The" in txt:
  print("Yes, 'free' is present.")



########################################################################################################
########################################################################################################

                  # Python - Slicing Strings

# You can return a range of characters by using the slice syntax.
# Specify the start index and the end index, separated by a colon, to return a part of the string.
# Example
# Get the characters from position 2 to position 5 (not included):

b = "Hello, World!"
print(b[2:5])

#-------------------------------------

            # Slice From the Start
# By leaving out the start index, the range will start at the first character:
# Example
# Get the characters from the start to position 5 (not included):

b = "Hello, World!"
print(b[:5])

#-------------------------------------

            # Slice To the End
# By leaving out the end index, the range will go to the end:
# Example
# Get the characters from position 2, and all the way to the end:

b = "Hello, World!"
print(b[2:])

#-------------------------------------

            # Negative Indexing
# Use negative indexes to start the slice from the end of the string:
# Example
# Get the characters:
# From: "o" in "World!" (position -5)
# To, but not included: "d" in "World!" (position -2):

b = "Hello, World!"
print(b[-5:-2])



########################################################################################################
########################################################################################################

                              # Python - Modify Strings
                
# Python has a set of built-in methods that you can use on strings.

            # Upper Case
# Example
# The upper() method returns the string in upper case:

a = "Hello, World!"
print(a.upper())


            # Lower Case
# Example
# The lower() method returns the string in lower case:

a = "Hello, World!"
print(a.lower())


            # Replace String
# Example
# The replace() method replaces a string with another string:

a = "Hello, World!"
print(a.replace("H", "J"))


# NOTE :- now learn about all string method

# To fix this problem, use the escape character \":
# Example
# The escape character allows you to use double quotes when you normally would not be allowed:

txt = "We are the so-called \"Vikings\" from the north."

# f string

name = "Rahul"
age = 21

# print("my name is ",name,"and my age is",age)
print(f"my name is {age} and my age is {name}")