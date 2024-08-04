# Default Constructor  

# class instace: 
#     def __init__(self,name): 
#          self.name = name 
#     def show(Raju): 
#          print(f"hii i am {Raju.name}") 
# p=instace(" sir m instance hu ") 
# p.show()  

#parameterized Construcotr   

# class Cou:  
#     count = "hello" 
#     def __init__(self): 
#         self.count+=" new"  
#         print(self.count)
#     def __del__(self): 
#         self.count-=" "  
#         print(self.count)
# p=Cou() 
 
#inheritance 

# class Introduction: 
#     def name_assign(self): 
#         self.name ="shreyank" 
     
# class Adding_Introductio(Introduction): 
#     def surname_assign(self): 
#         self.surname= self.name + "Agrawal"     
#         print(self.surname)
# p= Adding_Introductio() 
# p.surname_assign()  
    
 
#multilevel 
# class Man: 
#         @staticmethod 
#         def aadmi(): 
#             print("M ek aadmi hu") 
# class Women(Man): 
#         @staticmethod 
#         def aurat(): 
#             print("m ek aurat hu") 

# class Child(Women): 
#         @staticmethod 
#         def baccha(): 
#             print("m ek baccha hu") 

# c =Child() 
# c.aadmi() 
# c.aurat() 
# c.baccha()

# #multiple 
# class Man: 
#         @staticmethod 
#         def aadmi(): 
#             print("M ek aadmi hu") 
# class Women: 
#         @staticmethod 
#         def aurat(): 
#             print("m ek aurat hu") 

# class Child(Man ,Women): 
#         @staticmethod 
#         def baccha(): 
#             print("m ek baccha hu") 

# c =Child() 
# c.aadmi() 
# c.aurat() 
# c.baccha() 

#herarichal  
# class Man: 
#         @staticmethod 
#         def aadmi(): 
#             print("M ek aadmi hu") 
# class Women(Man): 
#         @staticmethod 
#         def aurat(): 
#             print("m ek aurat hu") 

# class Child(Man): 
#         @staticmethod 
#         def baccha(): 
#             print("m ek baccha hu") 

# c =Child() 
# c.aadmi() 

# w=Women() 
# c.aadmi()
 
#polymorhism  

# Compile Time polymorphism    

class Number : 
    def mark1(self,plastic): 
        self.plastic=plastic
        print(f"marks {self.plastic}") 
    def mark1(self): 
        print("Default marks 0 ") 
num =Number() 
num.mark1() 
num.mark1()



        