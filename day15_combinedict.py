#python code to combine two lists into a single dictionaty.
keys = ['ram', 'hari', 'shyam']
values = [10, 20, 30]
combine= dict(zip(keys, values))  # it return zip object

for i in range(len(keys)):  
    combine[keys[i]] = values[i]  
print("age:",combine)
