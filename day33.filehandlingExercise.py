# total number of character in the file
file_path = "newfile.txt"

character_count = 0

with open(file_path) as file:
	for line in file:
		character_count += len(line.replace(" ", "").strip("\n")) # replace all spaces and strip replace all newline
print(character_count)
#------------------------------------------------------------
#for copying content of file to another file
file_path = "newfile.txt"
copy_path = "newfile_copy.txt"

with open(file_path) as f, open(copy_path, "w") as c: #(,) should be put 
	for line in f:
		c.write(line) # this will write content in another file
#------------------------------------------------------------------
# for checking if the file exist or not
import os.path
file_path = "newfile.txt"
if os.path.isfile(file_path): #isfile or exists can be used to check if the file exists
	print("file_path already exists")
else:
	print("file_path does not exist")