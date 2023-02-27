
for i in (9,9,9,9,3,3,3):
    print("$"*i)
print("-------------------------------------------------------")

for i in range(7):
    for j in range(7):
        if i == 0 or i == 3 or i == 6:
            print("$", end="")
        elif i ==1 and j == 0:
            print("$", end="")
        elif i ==2 and j == 0:
            print("$", end="")
        elif i == 4 and j ==6:
            print("$", end="")
        elif i == 5 and j ==6:
            print("$", end="")
        else:
            print(" ", end="")
    print()
#------------------------------------------------------------------
#to print half pyramid
n = int(input("Enter the number of rows: "))

k = (2 * n) - 2

for i in range(n):

    for j in range(k):
        print("", end=" ")

    for j in range(i + 1):
        print("*", end=" ")

    print("")

    k = k - 2
#--------------------------------------------------------------
# to print the floyd's triangle
n=5
count=1
for i in range(1,n+1):
    for j in range(0,i):
        print(count, end=" ")
        count+=1
    print()