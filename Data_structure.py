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
first_set = set()
second_set = {1,1,1,1,1,1,2,2,2,0,"Ashu","ashu","ASHU","ASHU",True,True,False,False}
print(second_set)


# add element in set
first_set.add("Payal")
print("first_set", first_set)

# update element in set
first_set.update(["Payal","verma"])
print(first_set)

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