# python program to find the largest number among three numbers

num1,num2,num3 =input("enter three numbers:").split()
if num1>num2 and num1>num3:
    print(num1,"Is the largest")
elif num2>num3:
    print(num2,"is the largest")
else:
    print(num3,"is the largest")

# ------------------------------------------------------------------------------------
#largest number using function

def maximum(num1, num2, num3):
    if num1>num2 and num1>num3:
        largest=num1
    elif num2>num1 and num2>num3:
        largest=num2
    else:
        largest=num3
    return largest
print(maximum(40,20,10))

# ------------------------------------------------------------------------------------

def maximum(x,y,z):
    list=[x,y,z]    # we can also print the largest by using the max() function 
    return max(list)
print(maximum(10,20,30))
 
