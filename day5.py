# hacker rank problem 5 list comprehension
x = int(input())
y = int(input())
z = int(input())
n = int(input())
# for i in range(x+1):
#     for j in range(y+1):
#         for k in range(z+1):
#             if i+j+k !=n:
#                 print(list[i,j,k])

# list comprehension methods 
print(list([i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1)
if i+j+k !=n))
#---------------------------------------------------------------------------------

# more list comprehension examples
squared_numbers=[x**2 for x in range(10)]
print(squared_numbers)

