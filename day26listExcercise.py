# multiply each element in the list

list=[1,2,3,4,5,6,7,8]
factor=int(input("Enter a factor to multiply each element in the list: "))
# --------------------------------------------------------------
for i, elem in enumerate(list): #enumerate() return index and value
    list[i]=elem*factor
print(list)
# -------------------------------------------------
# print element in list without comma
list1=[1,2,3,4,5,6,7,8,9]
for i in list1:
    print(i,end=" ")
# ---------------------------------------------------------
# print element in list with its index
list1=[3,5,3,10,5,6,7,8]
for i, enum in enumerate(list): # enumerate function keep track index in list tuple  
    print(enum,i) # return the index i 
# ---------------------------------------------------------
# remove duplicates from list by dict function
list1=[3,5,3,10,5,6,7,8]
nodup=list(dict.fromkeys(list1))
# count the number of list item greater than 3
list=[1,2,3,4,5,6,7,8]
count=0
for i in list:
    if i>3:
        count+=1
print(count)
# ---------------------------------------------------------
# find the difference in list
list1=[1,2,3,4,5,6,7,8]
list2=[1,2,3,4,5]
difference1=[]
for i in list1:
    if i not in list2:
        difference1.append(i)
print(difference1)
# ---------------------------------------------------------
# to find the common element in the list
list1=[1,2,3,4,5,6,7,8]
list2=[1,2,3,4,5]
commonlist=[]
for i in list1:
    if i in list2:
        commonlist.append(i)
print(commonlist) 
# ---------------------------------------------------------
# to find the second largest value in list
list=[2,5,3,6,10,11,13,15,14,12,19]
sorted_list=sorted(list)
print(sorted_list[-2])
# ---------------------------------------------------------
# permutation of list
import itertools
my_list=[1,2,3]
prmute=list(itertools.permutations(my_list))
for permutation in prmute:
    print(permutation)