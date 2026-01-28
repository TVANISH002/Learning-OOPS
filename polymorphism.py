"""Polymorphism
Polymorphism is a core concept in Object-Oriented Programming (OOP) that allows objects of different classes to be treated as 
objects of a common superclass. It provides a way to perform a single action in different forms. Polymorphism is typically
achieved through method overriding and interfaces."""

"""Method Overriding
Method overriding allows a child class to provide a specific implementation of a method that 
is already defined in its parent class."""


## Base Class
class Animal:
    def speak(self):
        return "Sound of the animal"
    
## Derived Class 1
class Dog(Animal):
    def speak(self):
        return "Woof!"
    
## Derived class
class Cat(Animal):
    def speak(self):
        return "Meow!"
    
## Function that demonstrates polymorphism
def animal_speak(animal):
    print(animal.speak())
    
dog=Dog()
cat=Cat()
print(dog.speak())
print(cat.speak())
animal_speak(dog)

print("\n")
print("\n")
print("\n")



### Polymorphissm with Functions and MEthods
## base class
class Shape:
    def area(self):
        return "The area of the figure"
    
## Derived class 1
class Rectangle(Shape):
    def __init__(self,width,height):
        self.width=width
        self.height=height

    def area(self):
        return self.width * self.height
    
##Derived class 2

class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return 3.14*self.radius *self.radius
    
## Fucntion that demonstrates polymorphism

def print_area(shape):
    print(f"the area is {shape.area()}")


rectangle=Rectangle(4,5)
circle=Circle(3)

print_area(rectangle)
print_area(circle)





###Polymorphism with Abstract Base Classes
"""Abstract Base Classes (ABCs) are used to define common methods for a group of related objects. 
They can enforce that derived classes implement particular methods, promoting consistency across different implementations."""

from abc import ABC,abstractmethod

## Define an abstract class
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

## Derived class 1
class Car(Vehicle):
    def start_engine(self):
        return "Car enginer started"
    
## Derived class 2
class Motorcycle(Vehicle):
    def start_engine(self):
        return "Motorcycle enginer started"
    
# Function that demonstrates polymorphism
def start_vehicle(vehicle):
    print(vehicle.start_engine())

## create objects of cAr and Motorcycle

car = Car()
motorcycle = Motorcycle()

start_vehicle(car)








#from abc import ABC, abstractmethod

# # 1) Abstract Base Class 
# class BaseModel(ABC):

#     @abstractmethod
#     def fit(self, X, y):
#         """Train the model"""
#         pass

#     @abstractmethod
#     def predict(self, X):
#         """Make predictions"""
#         pass


# #  2) Concrete model #1
# class LogisticModel(BaseModel):
#     def fit(self, X, y):
#         print("Training Logistic Regression (dummy example)")
#         return self  # sklearn-style: return self

#     def predict(self, X):
#         return ["logistic_pred" for _ in X]


# #  3) Concrete model #2
# class TreeModel(BaseModel):
#     def fit(self, X, y):
#         print("Training Decision Tree (dummy example)")
#         return self  # sklearn-style: return self

#     def predict(self, X):
#         return ["tree_pred" for _ in X]


# #  4) One function that works with ANY model that follows the interface
# def train_and_predict(model: BaseModel, X_train, y_train, X_test):
#     model.fit(X_train, y_train)
#     return model.predict(X_test)


# #  5) Demo data (simple lists_beginner-friendly)
# X_train = [[1], [2], [3]]
# y_train = [0, 1, 1]
# X_test = [[10], [20], [30]]

# # 6) Use polymorphism: SAME function, DIFFERENT models
# log_model = LogisticModel()
# tree_model = TreeModel()

# log_preds = train_and_predict(log_model, X_train, y_train, X_test)
# tree_preds = train_and_predict(tree_model, X_train, y_train, X_test)

# print("\nLogisticModel predictions:", log_preds)
# print("TreeModel predictions:", tree_preds)
