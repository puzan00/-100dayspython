#use of replace function in string 
word='Hello, World'
# COMMA=','
# DOT='.'
print(word.replace(',','.')) #replace with dot 

#------------------------------------------------------
#to check if string contains all letters in alphabet
# import string
# word1="The quick brown fox jumps over the lazy dog"
# som=set(word1.lower())
# som.remove(" ")
# print(som==set(string.ascii_lowercase)) #this return true if the all alphabet are present in the string

#alternative method to check if the string is pangram
import string
word1="The quick brown fox jumps over the lazy dog"
is_pangram=True
for char in string.ascii_lowercase:
    if char not in word1.lower():
        is_pangram =False
print(is_pangram)
# ----------------------------------------------------------------------
#remove space in the string
word_remove="Hello, I am Nobody"
word_new=""
for char in word_remove:
    if char != " ":
        word_new+=char
print(word_new)
#-------------------------------------------------------
#to check if the string starts with prefix
word="hello"
prefix="he"
print(word.startswith(prefix))


    
