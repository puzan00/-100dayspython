#Polymorphism refers to the ability of different objects to be treated as if they are of the same type, 
# even if they are instances of different classes. This is achieved through inheritance and interfaces,
# which allow multiple classes to have common methods or attributes.
# polymorphism= many forms

# Types of polymorphism
#1.Duck typing
# 2.Operator typing
# 3.Method Overloading Polymorphism
# 4.Method Overriding Polymorphism

#method overloading
class MyClass:
    def my_method(self, arg1, arg2=None):
        if arg2 is not None:
            # handle case where two arguments are passed
            print("Two arguments: {}, {}".format(arg1, arg2))
        else:
            # handle case where only one argument is passed
            print("One argument: {}".format(arg1))

obj = MyClass()
obj.my_method(1)           # prints "One argument: 1"
obj.my_method(1, 2)        # prints "Two arguments: 1, 2"
#-------------------------------------------------------------------------
#method overriding
class Animal:
    def speak(self):
        print("The animal makes a sound")

class Dog(Animal):
    def speak(self):
        print("The dog barks")
        super().speak()   # call the original implementation in Animal

my_dog = Dog()
my_dog.speak()   # prints "The dog barks" followed by "The animal makes a sound"