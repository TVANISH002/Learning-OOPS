# #example 1

class BankAccount():
     def __init__(self, name, balance =0):
          self. name = name
          self.balance = balance
          pass
     
     def deposit(self, amount):
          self.balance = self.balance + amount
          print(f"{amount} is your desired amount and it is successfully deposited and your new balance is {self.balance}")
          
          
bank = BankAccount("mahesh", 10000)
bank.deposit(1000)      
print(bank.name)  


# #Example 2     
     
# class hyundai:
#      def __init__(self):
#           self.colour = "green"
#           self.price = 12356
#           self.mileage = 29
          
          
#      def cost(self, price):
#           print(f"the cost of the car is {price}")
           
# i20 = hyundai()
# i20.cost(i20.price)       



#EXAMPLE 3

# class Employee:
     
#      #magic method/special method/dunder method- constructor
#      def __init__(self):
#           #attributes
#           print("attributes started to initialize")
#           self.id=1
#           self.salary= 12345
#           self.designation = "ml"
#           print("attributes initialize successfully")
          
#      def travel(self, salary):  # function inside class is called method
#           print(f"i am earning {salary} and am travelling")
               
          
# #creating instance (i.e object) of the class  
# sam = Employee()

# #printing the attributes 
# #print(sam.id)

# #calling method
# sam.travel(sam.salary)
          
     

   
            