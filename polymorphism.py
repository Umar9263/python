# Python Polymorphism

# The word "polymorphism" means "many forms", and in programming it refers to methods/functions/operators with the same name that can be executed on many objects or classes.


# Function Polymorphism:-
# An example of a Python function that can be used on different objects is the len() function.

# String
# For strings len() returns the number of characters:

# Example:-
x = "Hello World!"

print(len(x))


# Tuple
# For tuples len() returns the number of items in the tuple:

# Example:-
mytuple = ("apple", "banana", "cherry")

print(len(mytuple))


# Dictionary
# For dictionaries len() returns the number of key/value pairs in the dictionary:

# Example
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(len(thisdict))


# Class Polymorphism
# Polymorphism is often used in Class methods, where we can have multiple classes with the same method name.

# For example, say we have three classes: Car, Boat, and Plane, and they all have a method called move():


# Example
# Different classes with the same method:

class Car:
  def _init_(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Drive!")

class Boat:
  def _init_(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Sail!")

class Plane:
  def _init_(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car class
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat class
plane1 = Plane("Boeing", "747")     #Create a Plane class

for x in (car1, boat1, plane1):
  x.move()


# Inheritance Class Polymorphism
# What about classes with child classes with the same name? Can we use polymorphism there?

# Yes. If we use the example above and make a parent class called Vehicle, and make Car, Boat, Plane child classes of Vehicle, the child classes inherits the Vehicle methods, but can override them:


# Example
# Create a class called Vehicle and make Car, Boat, Plane child classes of Vehicle:

class Vehicle:
  def _init_(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

class Car(Vehicle):
  pass

class Boat(Vehicle):
  def move(self):
    print("Sail!")

class Plane(Vehicle):
  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang") #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747") #Create a Plane object

for x in (car1, boat1, plane1):
  print(x.brand)
  print(x.model)
  x.move()


# Child classes inherits the properties and methods from the parent class.

# In the example above you can see that the Car class i empty, but it inherits brand, model, and move() from Vehicle.

# The Boat and Plane classes also inherit brand, model, and move() from Vehicle, but they both override the move() method.

# Because of polymorphism we can execute the same method for all classes.

# exemple:-

class exe:
  def show(self,name=""):
    print("hi "+ name)


obj=exe()
obj.show()
obj.show("vikas")  





# another example:-

class punjabi:
  def say_hello(self):
    print('ki hal chal ne')

class hindi:
  def say_hello(self):
    print('kase ho')

def ask(self):
  self.say_hello()# 4. object name dosen't metter it just call the say hello function


arshdeep = punjabi() # 1. arshdeep in intance of punjabi class 
rahul = hindi() # 2. rahul is intance of hindi class

ask(arshdeep) # 3. on this line python interpretor go on ask function.
ask(rahul)





class Parrot:
  def fly(self):
    print("Parrot can fly")
  def swim(self):
    print("Parrot can't swim")

class Penguin:
  def fly(self):
    print("Penguin can't fly")
  def swim(self):
    print("Penguin can swim")


# common interface
def flying_test(bird):
    bird.fly()

def swim_test(BIRD):
    BIRD.swim()

# make instance

Par = Parrot()
Pen = Penguin()

# passing the objects to the common function.

flying_test(Par)
swim_test(Pen)


# With for loop:-
class Parrot:
  def fly(self):
    print("Parrot can fly")
  def swim(self):
    print("Parrot can not swim")

class Penguin:
  def fly(self):
    print("Penguin can't fly")
  def swim(self):
    print("Penguin can swim")


# common interface
def flying_test(bird):
    bird.fly()

def swim_test(BIRD):
    BIRD.swim()

# make instance

Par = Parrot()
Pen = Penguin()
x=(Par,Pen)
# passing the objects to the common function.

for i in x:
   flying_test(i)
   swim_test(i)