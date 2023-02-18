# codewars questions
def century(year):
    return (year+99)//100 # adding 99 to the year //this a floor divisible
print(century(2001))

def is_divisible(n,x,y):
    #your code here
    if n%x==0 and n%y==0:
        return True
    else:
        return False
print(is_divisible(3,4,5))