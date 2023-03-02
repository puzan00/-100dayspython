# # def func(*args): # args in python allow to pass multiple arguments
def func(normal, *args):
    print(normal)
    for item in args:
        print(item)
normal=23
store=["pujan","pu","pjan","puja","puan","jan"]
func(normal,*store)
func(normal,"pujan","rujan","sujan","qujan","hero",12)
#---------------------------------------------------------------------
#kwargs in python allow to pass multiple keyword arguments to a function.
def my_func(**kwargs):
    for key ,value in kwargs.items():
        li.append([key,value])
    print(li)
li=[]
kw={"name":"pujan","age":20,"address":"chabil"}

# my_func(name=1,name2=2,name3=3)
my_func(**kw)
#---------------------------------------------------------------------

def func(kind,*args,**kwargs): #kind is normal, args take multiple arguments and kwargs take key value arguments
    print(f"--Do you want some {kind}?")
    print(f"--Do you want some extra {kind}?")
    for arg in args:
        print(arg)
    for kw in kwargs:
        print(kwargs)

args=["yes i want.","How much for the Cheese?"]
kwargs={"Cheese":"10$","Extra Cheese":"15$"}

func("Cheese", args, kwargs)