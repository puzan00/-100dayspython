# class Computer:
    def func(self): # self it the current object that we call
        print("Computer is a electronic device.")
    def __init__(self,ram,harddisk):  # define paramater for the instance variable
        self.ram = ram
        self.harddisk = harddisk
    def func(self): # self call itself 
        print("Computer:",self.ram,self.harddisk)
    
obj1=Computer(12,2) # this is the object of the class 
obj2=Computer(13,14) 
obj1.func() 
# obj1.func() 
#------------------------------------------------------------------------------------------------------------
# types of variable:
#1.class variable
#2.instance variable
#------------------------------------------------------------------------------------
class Computer():
    address="chabil" # class/static variable
    def __init__(self):
        self.name="pujan" # instance variable
        self.age=20
    def update(self):
        self.age=30
    def compare(self, other):
        if self.age==other.age:
            return True
        return False
c1=Computer()
c2=Computer()
c1.name="ram"
c1.update() # update function is call which will update the age
if c1.compare(c2): # this will compare self.age and other age (self is called for c1 and compared with c2)
    print("they are same")
else:
    print("they are different")

# print(c1.name,c1.address)
# # print(c1.age)
# print(c2.name,c2.address)
#---------------------------------------------------------------------------------------
# three types of method
# 1.instance method
# 2.class method
# 3.static method
#---------------------------------------------------------------------------------------
class School():
    Student="Ram"
    def __init__(self,s1,s2,s3): # instance method
        self.s1=s1
        self.s2=s2
        self.s3=s3
    
    def avg(self):
        return (self.s1+ self.s2+ self.s3)/3 # average of three numbers
    # def get_avg(self): # get method 
    #     return self.s1
    # def set_avg(self,value): #set method
    #     self.s1=value
    @classmethod #this is a decorator
    def get_student(cls): # this is a class method
        return cls.Student
    
    @staticmethod
    def info(): # this is a static method
        print("this is a School class")

s1=School(5,10,15) # object with the arguments
s2=School(11,13,20)
# s3=School(20,30,40)
print(s1.avg())
# print(s1.get_avg()) # this will give the value of s1 
print(School.get_student())
School.info()