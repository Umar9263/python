# Python Inheritance

# Python Inheritance:-
# Inheritance allows us to define a class that inherits all the methods and properties from another class.

# Parent class is the class being inherited from, also called base class.

# Child class is the class that inherits from another class, also called derived class.

# Create a Parent Class:-
# Any class can be a parent class, so the syntax is the same as creating any other class:-

# Example:-
# Create a class named Person, with firstname and lastname properties, and a printname method:

class Person:
  def _init_(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()





# Create a Child Class:-
# To create a class that inherits the functionality from another class, send the parent class as a parameter when creating the child class:

# Example
# Create a class named Student, which will inherit the properties and methods from the Person class:

class Person:
  def _init_(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  pass

x = Student("Mike", "Olsen")
x.printname()



# Now the Student class has the same properties and methods as the Person class.

# Example
# Use the Student class to create an object, and then execute the printname method:

class Person:
  def _init_(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  pass

x = Student("Mike", "Olsen")
x.printname()



# Add the _init_() Function
# So far we have created a child class that inherits the properties and methods from its parent.

# We want to add the _init_() function to the child class (instead of the pass keyword)

# Example
# Add the _init_() function to the Student class:

class Student(Person):
  def _init_(self, fname, lname):
    

    #add properties etc.
# When you add the _init() function, the child class will no longer inherit the parent's __init_() function.

# To keep the inheritance of the parent's _init() function, add a call to the parent's __init_() function:

# Example
class Person:
  def _init_(self, fname, lname):
     self.firstname = fname
     self.lastname = lname

  def printname(self):
     print(self.firstname, self.lastname)

class Student(Person):
  def _init_(self, fname, lname):
    Person._init_(self, fname, lname)

x = Student("Mike", "Olsen")
x.printname()



# Now we have successfully added the _init() function, and kept the inheritance of the parent class, and we are ready to add functionality in the __init_() function.


# Use the super() Function:-
# Python also has a super() function that will make the child class inherit all the methods and properties from its parent:

# Example
class Person:
  def _init_(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def _init_(self, fname, lname):
    super()._init_(fname, lname)

x = Student("Mike", "Olsen")
x.printname()


# By using the super() function, you do not have to use the name of the parent element, it will automatically inherit the methods and properties from its parent.

# Add Properties
# Example
# Add a property called graduationyear to the Student class:

class Person:
  def _init_(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def _init_(self, fname, lname):
    super()._init_(fname, lname)
    self.graduationyear = 2019

x = Student("Mike", "Olsen")
print(x.graduationyear)



# In the example below, the year 2019 should be a variable, and passed into the Student class when creating student objects. To do so, add another parameter in the _init_() function:

# Example
# Add a year parameter, and pass the correct year when creating objects:

class Person:
  def _init_(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def _init_(self, fname, lname, year):
    super()._init_(fname, lname)
    self.graduationyear = year

x = Student("Mike", "Olsen", 2019)
print(x.graduationyear)



# Add Methods
# Example
# Add a method called welcome to the Student class:

class Person:
  def _init_(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def _init_(self, fname, lname, year):
    super()._init_(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Mike", "Olsen", 2019)
x.welcome()

  

# If you add a method in the child class with the same name as a function in the parent class, the inheritance of the parent method will be overridden.