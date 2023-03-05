#understanding the lambda function
x=lambda a,b,c:a+b+c # lamda function take multiple arguments but perform single expression
print(x(2,4,6))

# def myfunc(n):
#   return lambda a : a * n
# mul=myfunc(2)
# print(mul(2))

# def a_first(list): # by usind def function 
#     return list[1]
list=[[2,5],[1,2],[3,3],[4,4]]
list.sort(key=lambda x:x[1]) # by using lambda function
print(list)



