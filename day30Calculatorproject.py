#take user input from user
num1 = float(input("Enter the first number: ")) 
num2 = float(input("Enter the second number:"))

#using def function for arithemtic calculation
def addition(num1, num2):
    return num1+num2

def difference(num1, num2):
    return num1-num2

def product(num1, num2):
    return num1*num2

def quotient(num1, num2):
    return num1/num2

#creating a choice for an operation
print("Choose an operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
#taking user input for the choice
input_choice = int(input("Enter the choice1-4: "))

# if the user choice match with the following condition it will perform following operation
if input_choice == 1:
    print("Sum:", addition(num1, num2))
elif input_choice == 2:
    print("Difference:", difference(num1, num2))
elif input_choice == 3:
    print("Multiplication:", product(num1, num2))
elif input_choice == 4:
    print("Divide:", quotient(num1, num2))
else:
    print("Invalid input!")
