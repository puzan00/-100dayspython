#add a key value pair in dictionary
# dict1={"jan":10,"feb":12,"mar":20}
# # dict1["april"]=30 # we can add key and value in this way
# new_key="april"
# new_value=30
# if new_key not in dict1:
#     dict1[new_key]=new_value
# print(dict1)

#merge dictionary 
# dict1={"ja":10,"fe":12,"ma":20}
# dict2={"jan":11,"feb":23,"mar":22}
# final_dict1= dict1 | dict2
# print(final_dict1)

# # maximum and minimum value in dictionary
# # dict1={"jan":11,"feb":23,"mar":22}
# # if dict1:
# #     max_value=max(dict1.values())
# #     min_value=min(dict1.values())
# # print(max_value)
# # print(min_value)

# # count  the frequency of value in dictionary
# dict1={"a": 1, "b": 2, "c":2,"d":4,"e":1,"f":4,"g":4,"h":6}
# fre_dict={}
# for value in dict1.values():
#     if value in fre_dict:
#         fre_dict[value]+=1
#     else:
#         fre_dict[value]=1
# print(fre_dict)

# #print maximum sum of values
# my_dict = {
# 	"a": [1, 2, 3],
# 	"b": [4, 0, -4],
# 	"c": [300, 5, 9],
# 	"d": [45, 12, 100]
# }

# max_sum = None

# for list_value in my_dict.values():
# 	list_sum = sum(list_value)

# 	if max_sum is None:
# 		max_sum = list_sum
# 	elif max_sum < list_sum:
# 		max_sum = list_sum

# print(max_sum)
# # sort the list in dictionary
# my_dict = {
# 	"a": [4, 3, 2],
# 	"b": [5, 3, 7],
# 	"c": [1, 9, 10],
# 	"d": [3, 4, 1]
# }

# for list_value in my_dict.values():
# 	list_value.sort()

# print(my_dict)

# dictionary into list
product_info = {
	"description": "shoe",
	"price": 4.56,
	"colors": ["green", "blue", "red"],
}
list2=[]
for key, value in product_info.items():
	list2.append([key,value])
print(list2)