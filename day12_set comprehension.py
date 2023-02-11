# set comprehension example
def func(y):
    return list(
        {
            x for x in y if y.count(x)>1
        }
    )
y=[1,2,2,3,4,4,5,6,7,7]
print(func(y))
#-----------------------------------------------------------------------
# more examples
list=[1,2,3,4,5,6,7]
new_set={x*5 for x in list if x%2==0}
print(new_set)