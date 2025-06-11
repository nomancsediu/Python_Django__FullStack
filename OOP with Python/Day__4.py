
class Animal:
  def make_sound(self):
    print("The animal makes a sound")

class Dog(Animal):
  def make_sound(self):
    print("The dog barks")

class Cat(Animal):
  def make_sound(self):
    print("The cat meows")

# Polymorphism in action
animals = [Dog(), Cat()]

for animal in animals:
  animal.make_sound()

class Shape:
  def area(self):
    print("Calculating area...")

class Circle(Shape):
  def area(self):
    print("Area of a Circle: pi*r*r")

class Square(Shape):
  def area(self):
    print("Area of a Square: side*side")

# Polymorphism in action
shapes = [Circle(), Square()]

for shape in shapes:
  shape.area()

class Bird:
  def make_sound(self):
    print("Bird chirps!")

class Duck:
  def make_sound(self):
    print("Duck quacks!")

def animal_sound(animal):
  animal.make_sound()

# Polymorphism in function arguments
bird = Bird()
duck = Duck()

animal_sound(bird)
animal_sound(duck)

# Animal Sound Simulator

#Base Class
class Animal:
  def make_sound(self):
    print("Some generic animal sound")

# Derived Classes
class Dog(Animal):
  def make_sound(self):
    print("Woof! Woof!")

class Cat(Animal):
  def make_sound(self):
    print("Meow! Meow!")

class Cow(Animal):
  def make_sound(self):
    print("Moo! Moo!")

class Duck(Animal):
  def make_sound(self):
    print("Quack! Quack!")

# Simulator Class
class AnimalSoundSimulator:
  def __init__(self):
    self.animals = []

  def add_animal(self, animal):
    if isinstance(animal, Animal):
      self.animals.append(animal)
      print(f"{animal.__class__.__name__} added to the simulator")
    else:
      print("Invalid animal type")

  def make_all_sounds(self):
    if not self.animals:
      print("No animals in the simulator")
    else:
      print("\n--- Animal Sounds ---")
      for animal in self.animals:
        animal.make_sound()

#Main Program
simulator = AnimalSoundSimulator()

while True:
  print("\n--- Animal Sound Simulator ---")
  print("1. Add Dog")
  print("2. Add Cat")
  print("3. Add Cow")
  print("4. Add Duck")
  print("5. Make All Sounds")
  print("6. Exit")

  choice = input("Enter your choice (1-6): ")

  if choice == '1':
    simulator.add_animal(Dog())
  elif choice == '2':
    simulator.add_animal(Cat())
  elif choice == '3':
    simulator.add_animal(Cow())
  elif choice == '4':
    simulator.add_animal(Duck())
  elif choice == '5':
    simulator.make_all_sounds()
  elif choice == '6':
    print("Exiting the simulator. Goodbye!")
    break
  else:
    print("Invalid choice. Please try again.")