# print fibonacci serries by for loop

first=0
second=1
print(first)
print(second)

for i in range(1,9):
    third =first + second
    print(third)
    first,second =second,third

# print fibonacci serries by function
def fibonacci(n):
    num1 = 0
    num2 = 1
     
    # Check is n is less than 0
    if n < 0:
        print("Incorrect input")
         
    # Check is n is equal to 0
    elif n == 0:
        return 0
       
    # Check if n is equal to 1
    elif n == 1:
        return num2
    else:
        for x in range(1, n):
            num3 = num1 + num2
            num1=num2
            num2=num3
            print(num2)
        
print(fibonacci(14))
