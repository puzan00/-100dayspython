#distance between two points
import math
x1,y1=3,2
x2,y2=9,7
distance=math.sqrt((x2-x1)**2+(y2-y1)**2)
print(distance)
#-------------------------------------------------------------------------

#by taking user input
x1 = float(input("Enter the x-coordinate of the first point: "))
y1 = float(input("Enter the y-coordinate of the first point: "))
# Take input from the user for the second point
x2 = float(input("Enter the x-coordinate of the second point: "))
y2 = float(input("Enter the y-coordinate of the second point: "))
distance=math.sqrt((x2-x1)**2+(y2-y1)**2)
print(distance)

#----------------------------------------------------------------------
# by using function
def distance(x1, y1, x2, y2):
  return (((x2 - x1)**2 +(y2 - y1)**2)**0.5)
print( distance(3, 4, 4, 3))
