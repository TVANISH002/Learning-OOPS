# ###INHERITANCE

#  #SINGLE_Only one child is inheriting from parent class
# #Parent class
# class Car:
#      def __init__(self, windows, doors, engine_type):
#           self.windows = windows
#           self.doors = doors
#           self.engine_type = engine_type
          
#      def drive(self):
#           print(f" he drives {self.engine_type}  car, which has {self.doors} doors in it")
          
# model1 = Car(10,5,"Petrol")
# model1.drive()               
          
          
#  #child class
 
# class tesla(Car): # write parent class name in parenthesis_this inherits all parent class to child 
#       def __init__(self, windows, doors, engine_type, is_electric ): #parents attributrs +childs attributes
#            super().__init__(windows, doors, engine_type) #inherits parents attributes
#            self.is_electric = is_electric
           
#       def electric(self):
#            print(f"Tesla is electric : {self.is_electric} " )
           
# model_x = tesla(10,5,"electric", True)
# model_x.electric()  
# model_x .drive()         #calling methods from parenet class 




#MULTIPLE_ when a class inherits fro more than one base class

#Base class 1
class animal:
     def __init__(self, dog_name):
          self.dog_name = dog_name
     def speak(self):
          return f"subclass mult implement thsi method"
     
#Base class 2
class Pet:
     def __init__(self, caretaker):
          self.caretaker = caretaker
  

#Derived class

class dog(animal, Pet):
     def __init__(self, dog_name, caretaker):
          animal.__init__(self, dog_name)
          Pet.__init__(self,caretaker)
          
     def speak(self):
          return f"{self.dog_name} say woof-woof"     
          

obj1 = dog("buddy", "cheddy")
print(obj1.speak())
print(obj1.caretaker)
print(obj1)
print(f" the owner of {obj1.dog_name} is {obj1.caretaker}")
                         
               