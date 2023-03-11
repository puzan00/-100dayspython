# #recursion
# Recursion is a programming technique in which a function calls itself repeatedly until a base case is reached. 
# It is a powerful and elegant way to solve certain types of problems, 
# such as those involving tree structures, backtracking, and divide-and-conquer algorithms.
#----------------------------------------------------------------
# factorial of a number
def factorial(num):
    if num == 0 :
        return 1 
    return num * factorial(num-1) # calling function itself
output=factorial(5)
# print(output)

# binay search
# 
def binary_search(arr, x):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1
arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
x = 14
print(binary_search(arr,x))
