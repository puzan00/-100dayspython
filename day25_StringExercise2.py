#reverse a string 
s="hello world"
s1=""
word_list=s.split(" ")
for item in word_list:
    reversed_word=item[::-1] # it return reversed string
    Swap_case=reversed_word.swapcase() #swap case change upper to lower and vice versa
    s1+=Swap_case+ " " # adding the new value to the s1 string
print(s1)
#------------------------------------------------------------------
#count the repeat numbers of char and display the repeated char
s = "HelloOhmygod"
repeated_count = 0
repeated_chars = []

for char in s:
	if (s.count(char) > 1) and (char not in repeated_chars):
		repeated_count += 1
		repeated_chars.append(char)

print(repeated_count)
# print(repeated_chars)
if len(repeated_chars)>0: 
	print(*sorted(repeated_chars), end=" ") # One line, avoid loop
else:
	print(None)
# ---------------------------------------------------------------------------
#sort words in string
s="hey you are beautiful"
n_words=""
split_words=s.split(" ")

for i in split_words:
    upper_case=i.upper()
    sorted_words="".join(sorted(upper_case))
    n_words+=sorted_words+" "
print(n_words)