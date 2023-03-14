#codewar 8kyu problems

#checking the case of character
def same_case(a, b): 
    # your code here
    if not(a.isalpha() and b.isalpha()):
        return -1
    elif a.islower()==b.islower():
        return 1
    else:
        return 0
#---------------------------------------------------------------------------
#Given a month as an integer from 1 to 12, return to which quarter of the year it belongs as an integer number.
def quarter_of(month):
    return (month - 1) // 3 + 1
#----------------------------------------------------------------------------

# father is twice then son in ....year
def twice_as_old(dad_years_old, son_years_old):
    years_ago = abs(dad_years_old- 2*son_years_old)
    return years_ago
#------------------------------------------------------------------------
#if you can't sleep count the sleep
def count_sheep(n):
    murmur=""
    for i in range(1,n+1):
        murmur+= str(i) +" sheep..."
    return murmur
num = 3
print(count_sheep(num))
#--------------------------------------------------------------------
#students final grade
def final_grade(exam, projects):
    if exam > 90 or projects > 10:
        return 100
    elif exam > 75 and projects >= 5:
        return 90
    elif exam > 50 and projects >= 2:
        return 75
    else:
        return 0
