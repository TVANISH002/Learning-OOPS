class chatbook:
     def __init__(self):
          self.username = ""
          self.password = ""
          self.loggedin = False
          self.menu()
          
     def menu(self) :
          userinput = input(""" Please select from follwoing options:
                1. signup press 1
                2.login
                3.post something
                4.chat with friends
                5.logout \n""")
                
          if  userinput == "1":
               
               self.signup()
          elif userinput == "2":
               self.login()
          elif userinput == "3":
               self.post()
          elif userinput == "4":
               self.chat()
          elif userinput == "5":
               self.logout()
          else :
               print("invalid")
               self.menu()
                    

     def signup(self) :
          email = input("write ur email: ")
          pswd = input("write ur password: ")
          self.username = email
          self.password = pswd
          print("sighnup successful")
          print("\n")
          self.menu()
     
     
     def login(self):
          if self.username == "" and self.password == "":
               print("please signup first")
               self.menu()
          else:
               usname = input("write ur emailusername: ")
               password = input("write ur password: ")
               if self.username == usname and self.password == password:
                    self.loggedin = True
                    print("login successful")
                    self.menu() 
               else:
                    print("invalid credentials")
                    self.menu()
               
     def post(self):
          if self.loggedin == True:
               tobe_printed = input("please type to post: ")
               print(f" u have successfully posted and it has {tobe_printed}")
               self.menu()
          else:
               print("kindly create an account and then post")   
               self.menu()  
               
     def chat(self):
          if self.loggedin == True:
               user1 = input("write something to ur friend :")
               user_detail = input("write ur friend name")
               print(f" your message was sent successfully to {user_detail}")    
               self.menu()
          else:
               print("please create account and then continue")
               print("\n" )
               self.menu()     
                         
                    
     def logout(self):
          self.loggedin = False
          print("thanks for using our platform, come visit us again")
          self.menu()
         
               
letsgo = chatbook()          
              