# # x = 10 int
# # y = 12.3 float
# # flag = True/False bool
# # is  

# # implicitly and explicitly 
# x = 10 + 12.5
# print(type(x))

# # x = "abc" + 10

# x = 10 + True
# print(type(x),x)

# # type converstion
# x = 10
# print(float(x))
# print(str(x))
# print(bool(x))

# # falsy values 
# # 0, '', 
# x= -3
# x = 0
# print(bool(x))

# # .pyc
# print("hello world")
# # asdfkl
"""
None

False

0 (integer zero)

0.0 (float zero)

0j (complex zero)

'' or "" (empty string)

[] (empty list)

{} (empty dictionary)

() (empty tuple)

set() (empty set)

"""
# num = 0
# num2 = None
# num3 = 0.0
# strng = ''
# li = []
# dic = {}
# _set = set()
# _tup = ()


# api call
# data = api()



# ----operators 
# arthematic
# +,-,*,/,%,
# // (floor division)
# print(5/2)
# 2.5
# print(5//2)
# 2

# # //=	Floor divide and assign	x //= 2

# num = 10
# num = num /2
# num /= 2
# # %=	Modulus and assign	x %= 2
# num %= 2
# # **=
# num **= 2

# && , || , !
# and , or , not

# 1, 2, 4, 8, 16 ,32 ,64, 128
# 8 =  0 |0 | 0| 1| 0
# 21 = 1 |0 | 1 |0 |1
# -------------------
#                 0|0|0|0|0 = 0


# 1 & 1 = 1
# 0 & 1 = 0

# print(8 & 21)

# identity (is)
x = 8 
y = x 
y = 12
print( x is y)

# membership ( in )
# print('a' in "apple")
# print('z' in "apple")
# li = [1,2,3,4]
# print( 8 in li)

# true_value if condition else false_value


# flow control 
#  if else 
#  if elif else

# loop 
#  for , while
#  break , continue
# x = 1
# while x < 10 :
#     if x % 2 == 0 :
#         x+=1
#         continue
#     print(x)
#     x+=1

# while True:
#     print("hello")
#     break
# else:
#     print("world")

# data structure in python 
#  list, dictionary , tuple , set,frozen set
#  list = []
# list = list()
# mutable(changable), ordered(index), index = 0

#  dictionary (object)
dic = {"key" : 12}
# mutable
# key value pair data store, items(), key(), values()

# tuple
# imutable , ordered
# tup = (1,2,3)
# print(type(tup), tup)
# print(tup[0])


# set 
# mutable , unordered
# _set = {1,2,3,4}
# print(type(_set),_set)
# print(type(_set),_set)

# num = 10
# num = (10)
# print(type(num), num)

# tup = ("asu39347285" ,)
# print(type(tup))


# continue 
# for i in range(10):
#     if True:
#         # print(i)
#         if i == 2:
#             continue
#         print("inside",i)
#     print("outside")

# for , while , while/else
# i = 1
# while i < 2:
#     print(i)
#     break
# else:
#     print("falsy condition")

# Built -in -data structure.
# list
li = [1,2,3,"Payal",True, 10.26,[4,3,2,["Orange"]]]
print(li[0])
print(li[6][3])

print("reverse indexing",li[-1])
print(len(li))

# slicing the list
li = [0,1,2,3,4,5,6,7,8]
# [start : end : step]
# start ---> by default 0 , end = len(list)
# end = stop value (exclusive)
# step = 1
print("left to right",li[1:5:2])

print("without start",li[:4])
print("without end",li[1:])
print("without end",li[1: : 2])
print("without start and end",li[::4])

# reverse slicing
print("reverse slicing",li[8 : 0 : -1])
print("without start slicing",li[8 : : -1])

# reverse a list
print("reverse the list ",li[::-1])
print("*"*10)

# list methods
# add single element
li = [1,2,3]
# li.append([4,5])
# print("list append",li)

# adding whole new list
li2 = [5,6,7]
li.extend(li2)
print(li)

# on an specific index 
li.insert(0,"start")
li.insert(0,"start")
print(li)

# delete
# li = [1,2,3,4,5,6,7,8,9]
# li.clear()
# li2 = li.copy()
# count the number of occurance
# li = [2,2,2,2,2,3,3,3,3,4,4,4,5,5,6,7,8,9]
# print(li.count(19))

# find the index of perticular element
li = [1,2,3,33,4,5,2,2,2,2,6,86,4,3,4,23,54,65,2]
# print(li.index(2)) # index first occur

# print(li.pop()) #always last element
# print(li.pop(2)) # specific index
# print(li)

# li.remove(2) # remove perticular element
for i in range(li.count(2)):
    li.remove(2)
print(li)

# sort 
# li = [32,1,23,54,2,5,2,4,6.6]
# li.sort() # by default ascending order
# li.sort(reverse=True) # decending order

# li = ["Ash","Tanuja","Z","Zomat"]
# li.sort(key=len)

# problem with sort
# li = [1,2000,30,50,55.4]
# li.sort()
# print(li)
# sorted
# sorted(li)
# reverse
# li = [1,2,3,4,5]
# li.reverse()
# print(li)
# li = list((1,2,3,4,5))
# print(li)

# ------
# li = [
#     1,2,3,4,5,6
# ]
# print(li.remove())
