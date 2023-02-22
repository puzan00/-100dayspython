#to check list is empty or not
l1 = ["bmw", "rolls royce", "honda", "toyota", "suzuki"]
l2 = []
if len(l2)==0:
    print("list is  empty")
else:
    print("list is not empty")
#---------------------------------------------------------------------------
# to remove duplicates in list
list1=[1,2,3,4,5,6,7,8,9,4,3,2,1]
list2=set(list1)
print(list(list2))
#-----------------------------------------------------------------
my_list = [1,2,2,3,1,4,5,1,2,6]
myFinallist = []
for i in my_list:
    if i not in myFinallist:
        myFinallist.append(i)
print(list(myFinallist))
