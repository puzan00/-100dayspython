# factorial of user input by conditional expression
num=int(input("enter a number:"))
fact=1
if num<=0:
    print("Enter a valid number!")
else:
    for i in range(1,num+1):
        fact=fact*i
        print(fact)
#---------------------------------------------------------------------

# factorial using recursion to print a factorial number of user input.
n=int(input("Input a number to compute the factiorial : "))
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(n))