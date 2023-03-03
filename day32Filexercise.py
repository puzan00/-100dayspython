# for the reading the file in list
file_path="newfile.txt"
file_content=[]

with open(file_path,'r') as f: # for reading the file 
    for i in f:
        file_content.append(i)
print(file_content)

with open(file_path,'w')as f: 
    f.write("hey don't go there I am here\nhey he is shyam") # for writing content in file
# print(file_content) # this will show the content of file
# print(f.closed) # for checking if the file is closed

with open(file_path,'r') as f: 
    for i in f:
        print(i,end='') # reading the content of the file 
#------------------------------------------------------------------------------
#read firstline in the file

file_path='newfile.txt'
n=int(input("how many line do you wnat to read:"))
print("-------------------------------------------------------------------")

with open(file_path, 'r') as f:
    lines=f.readlines()
    n_line=len(lines)

    if n_line<n:
        print(f"Please enter the number again. File contain {n_line}")
    else:
        for i in range(n,0,-1): # this will print in reverse order
            print(lines[i].strip("\n"))

#-------------------------------------------------------------------
# for printing the longest word in the file
file_path='newfile.txt'
longest_words=""
with open(file_path, 'r') as f:
    for word in f:
        if len(word)>len(longest_words):
            longest_words=word
print(longest_words)