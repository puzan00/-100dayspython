# hackerrank swap case
def swap_case(s):
    x=''
    for i in s:
        if i.isupper():
            i=i.lower()
        else:
            i=i.upper()
        x +=''.join(i) #it join all the element of string with concatenation 

    return x
if __name__ == '__main__':
    s = input("Enter any string:")
    result = swap_case(s)
    print(result)
#-----------------------------------------------------------------------------------------------
# join with dictionary
dict={"Name":"ram", "age":"20","city":"ktm"}
d="---"
x=d.join(dict.values())# it works in string
print(x)