# =====================================================
# 📘 Assignment 1 & 🎭 Activity 2: OOP Practice in Python
# =====================================================

# ------------------------------
# Part 1: Design Your Own Class 🏗️
# ------------------------------

class Smartphone:
    def __init__(self, brand, model, storage):  # constructor to initialize
        self.brand = brand
        self.model = model
        self.storage = storage
    
    def call(self, number):
        print(f"{self.brand} {self.model} is calling {number}... 📞")
    
    def take_photo(self):
        print(f"{self.brand} {self.model} is taking a photo! 📸")


# Inheritance Example (Smartwatch IS-A Smartphone)
class Smartwatch(Smartphone):
    def __init__(self, brand, model, storage, strap_color):
        super().__init__(brand, model, storage)  # use Smartphone constructor
        self.strap_color = strap_color
    
    # Override the call method (Polymorphism)
    def call(self, number):
        print(f"{self.brand} {self.model} smartwatch is calling {number} on speaker! 🎙️")


# ------------------------------
# Part 2: Polymorphism Challenge 🎭
# ------------------------------

class Animal:
    def move(self):
        print("This animal moves in some way...")

class Dog(Animal):
    def move(self):
        print("Dog is running 🐕")

class Bird(Animal):
    def move(self):
        print("Bird is flying ✈️")

class Fish(Animal):
    def move(self):
        print("Fish is swimming 🐟")


# ------------------------------
# Testing Everything 🚀
# ------------------------------

# Assignment 1 Test
print("=== Smartphone & Smartwatch Demo ===")
phone1 = Smartphone("Apple", "iPhone 15", "256GB")
watch1 = Smartwatch("Samsung", "Galaxy Watch", "32GB", "Black")

phone1.call("123-456")
phone1.take_photo()
watch1.call("987-654")

# Activity 2 Test
print("\n=== Polymorphism Demo ===")
animals = [Dog(), Bird(), Fish()]

for animal in animals:
    animal.move()
