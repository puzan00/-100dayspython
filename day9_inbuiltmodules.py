# basic inbuilt modules example
help('modules') # it shows the list of all modules 
# --------------------------------------------------------------
import calendar  # to  show the calender in month
print(calendar.month(2023,1))
# --------------------------------------------------------------
import time
# print(time.localtime()) # provide all detail day and time 
print("Hello")
time.sleep(2) # sleep for 2 seconds
print("World")
# --------------------------------------------------------------
import keyword # to show the list of keywords
print(keyword.kwlist)
# --------------------------------------------------------------
import random
random_num=random.randint(0,10)
# rand=random.random()*100
list=["Ram","hari","Shyam","Laxman","Bikash","ujjwal"]
choice=random.choice(list)
print(choice)
# --------------------------------------------------------------
import math
num=math.sqrt(12) # square root
# num=math.e #show exponential
print(num)
