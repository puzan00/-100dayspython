#inheritance basic concept in python 
# inheritance:Inheritance is a OOPconcepts that allows a new class to be based on an existing class,
#inheriting its attributes and methods. 
# The existing class is called the parent class or superclass, and the new class is called the child class or subclass.
#----------------------------------------------------------------
class A: #super class single level inheritance

    def feature1(self):
        print("this is a feature1") 
    def feature2(self):
        print("this is a feature2")
class B(A): # subclass of A  
    def feature3(self):
        print("this is a feature3")
    def feature4(self):
        print("this is a feature4")
class C(B): # multilevel inheritance
    def feature5(self):
        print("this is a feature5")
    
# a1=A()  # a1 can access feature1and 2
# b1=B() # b1 can access feature1,2,3,4
# c1=C() # c1 can access feature1,2,3,4,5
# c1.feature1() 
#-------------------------------------------------------------------------
# constructor in inheritance
class A: #super class single level inheritance
    def __init__(self):
        print("this is a init method")
        
    def feature1(self):
        print("this is a feature1") 
    def feature2(self):
        print("this is a feature2")
class B: # subclass of A  
    def __init__(self):
        # super().__init__() it calls the superclass constructor
        print("this is B init method")
    def feature3(self):
        print("this is a feature3")
    def feature4(self):
        print("this is a feature4")
class C(A,B): 
    def __init__(self):
         super().__init__() # this is call superclass constructor ie. A
         print("this is C init method")
    def feature5(self):
        print("this is a feature5")

a1=C()
print(C.mro())