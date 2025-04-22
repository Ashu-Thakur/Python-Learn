# Dictionary
dic = {
    "Name" :"Payal",
    "Age" : 24
}
print(dic)

# find out keys
print(dic.keys())

# find values
print(dic.values())

# key and values
print(dic.items())

# specific value
print(dic["Age"])
print(dic["Name"])
# throws error when specific key doesn't exist
# print(dic["Gender"])
print(dic.get("Age", "Nothing"))
print(dic.get("Gender", "Nothing"))


# add, append
dic["Age"] = 23
dic["age"] = 23
print(dic)

# nested structure
dic["specific_data"] = {"Hobbies":["singing", "dancing"]}
print(dic)
print("Hobbies-->",dic["specific_data"]["Hobbies"][1])

# delete
# del dic["age"]
# print(dic)

# delete whole dictionary
# del dic

# # clear
# dic.clear()
# print(dic)

# pop the perticular key value
# dic.pop("age")
# print(dic)

# pop item
dic.popitem()
print(dic)

# update the dictionary 
# dic.update({"tech":"IT"})
# dic.update({"Age":"IT"})
# print(dic)


# Iteration over dictionary
for key in dic:
    print(f"{key} : {dic[key]}")

for value in dic.values():
    print(f"values : {value}")


# for key value both
# first, second = 10,20
# print(dic.items())
#[('Name', 'Payal'), ('Age', 23), ('age', 23)]
# for key, value in dic.items():
#     print(key, value)
     #('Name', 'Payal')

# dic = {"name":"Payal Verma", "Age":24}
# if "name" in dic:
#     dic["first_name"] = dic["name"].split(" ")[0]
#     dic["second_name"] = dic["name"].split(" ")[1]
#     dic.pop("name")
# print(dic)

####### SET #########
# first_set = set()
# second_set = {1,1,1,1,1,1,2,2,2,0,"Ashu","ashu","ASHU","ASHU",True,True,False,False}
# print(second_set)


# add element in set
# first_set.add("Payal")
# print("first_set", first_set)

# update element in set
# first_set.update(["Payal","verma"])
# print(first_set)

# remove element from set
# first_set.discard("Ashu")
# first_set.discard("verma")
# print(first_set)

# second_set = {1,2,3,4,5}
# for index, value in enumerate(second_set):
#     print(index, value)

# Tuple
# tup1 = tuple((1,2,3,4,5))
# tup2 = (1,2,3,4,5)
# tup3 = (1,)
# print(type(tup1),type(tup2),type(tup3))

# print(tup1[0])
# print(tup1.count(2))
# print(tup1.index(5))

# li = [2,2,4,4,1,2,4,6,3,4,6,3,2,1]
# """
# {
# "1" : 2,
# "2":4
# }
# """
# dic = {}
# for i in li:
#     dic[i] = li.count(i)
# print(dic)

# ----------------------------------------------------------------------------------------------

di = {"name":"payal","age":24}

if "name" in di:
    print(di["name"])

# string
# first_name = "payal"
# second_name = "Verma"

# print(first_name + second_name)
# print("first character",first_name[0])
# print("last_character",first_name[-1])

# sub string
# email = "ashuthakur07@gmail.com"
# print("first_name",email[:10])
# string = "NOONE"
# if string == string[::-1]:
#     print("palindrom")

# string is imutable
string = "Hello world"

print('h' in string)
print('h' not in string)

string = "the price of this product is \" "
print(string)

# string methods

string = "HeLLo World"
print(string.swapcase())

# trim whitespace the string 
string = " Hello World "
print(f"start and end :{string.strip()}")
print(f"start :{string.lstrip()}")
print(f"end :{string.rstrip()}")

# split the string 
string = "H_ello_worl-d"
print(string.split(" "))
print(string.split("_"))
print(string.split("H"))

# reverse the string
# string = "The Quick brown fox jumps over the lazy dog"
# list_of_string = string.split(" ")
# print(list_of_string)
# list_of_string.reverse()
# print(list_of_string)
# reverse_list = "-".join(list_of_string)
# print(reverse_list)
# print("----------------------------")
# reverse_string = "-".join((string.split(" ")))
# print(reverse_string)

# print(string.find("brown",17)) # if the substring doesn't exist in the main string it returns -1

# new_string = "Hello_World"
# print(new_string.replace("ll","yy"))
# print(new_string.replace("l","yy",2))

# character to ascii
print("----------------------------")
char = 'A'
print("ascci value of any character :",ord(char))

# ascii to character
number = 75
print("ascii into character :",chr(number))

