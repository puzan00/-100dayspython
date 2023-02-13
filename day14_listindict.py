#using list in dictionary 
best_program_lang={
    "ujjwal":["python","java","C"],
    "shyam":["java","javascripts","php"],
    "rohit":["c#","kotlin"]
    }
for i,j in best_program_lang.items():
    print("----------------------------------------------")
    print(f"the best programming language of {i} is:")
    
    for k in j:
        print(k)