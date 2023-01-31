# program to check if the user number is prime number.

num = int(input("Enter a number:"))  # using for loop

if num > 1:  # check if the user given number is greater than 1  if not run else statement
    for i in range(2, num):
        if num % i == 0:
            print(num, " is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")
#---------------------------------------------------------------------------------
# using def function to check if the number is prime

def isprime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True
print(isprime(10))
#--------------------------------------------------------------------------------

# print prime number in given range
lower = int(input("Enter the lower value:"))
upper = int(input("Enter the upper value:"))
for num in range(lower, upper+1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)
#---------------------------------------------------------------------------------
# print prime number up to 100
num = 100
for num in range(2, num):
    for i in range(2, num+1):
        if num % i == 0:
            break  # stop the loop if it meets the condition
    else:
        print(num)
