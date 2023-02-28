# to check vowel or consonant
text="score2"
for char in text.lower():
    if char in ("a","e","i","o","u"):
        print(f"{char} is vowel")
    elif not char.isalpha():
        print(f"{char} is not letter")
    else:
        print(f"{char} is a consonant") 
#------------------------------------------------------------------
# increasing and decreasing order
a,b,c=5,10,14
if a>b>c:
    print("decreasing order")
elif a<b<c:
    print("increasing order")
else:
    print(None)
#------------------------------------------------------------------
#check if the year is the leap year or not 

year=1600
if year%4==0:
    if year%100==0:
        if year %400==0:
            print("year is a leap year")
        else:
            print("year is not a leap year")
    else:
        print("year is a leap year")
else:
    print("year is not a leap year")        
