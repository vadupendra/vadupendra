'''
# ! ----> problem:1
s1 = {1,2,3,4,5}
s2 = {3,2,7,8,9}

# n1 = {1,2,3} -------> s1

for val in s1:
    if val in s2:
        str1="i hate you"
print(str1)
''

# ! -------> dictionary
# eg:1
d1 = {1:100, 'a':200, 4.5:"hello"}
print(d1)
print(len(d1))

''
mech_name =["name1", "name2", "name3"]
mech_age = [23,22,24]
mech_mark = [89,78,60]
mech_email = ["name2@gmail.com", "name3@gmail.com"]


# ? char of dictionary
# 1.) have to be surrounded by {}
# 2.) It have to be in the form of key, valye pair
# 3.) It is mutable
# 4.) duplicate keys are not allowed, duplicate values are allowed
# 5.) It is unindexed
# 6.) It is ordered
# 7.) Key does not allow mutable datatypes, values allowmutable datatype


d1 (1:100, 2:200, 3:300, 4:400)
#to access elemenst in dictionary

print(d1)
or
To access the values, have to use key
print(d1[1]) # o/p 100
''

#? some common functions
# len(), min, max()
print(min(d1))
print(max(d1))
''

# ? to find min, max based on values
print(min(d1.values()))
print(max(d1.values()))
''
# ? dictionary based funtions
# to add element(key and value pair) in dict
d1 = {1:100,2:200,3:300,4:400}
d1[5] =500
pint(d1)
''
# ? to replace a value in dictionary
d1 = {1:100,2:200,3:300,4:400}
d1[2]="mango"
print(d1)
''




#? delete element from dictionary
d1 (1:100, 2:200, 3:308, 4:400)
# popitem()
# to delete last key value pair in dict
# d1.popitem()
# print(d1)
# pop()
# d1.pop(2)
# 2 is the key in dictionary
# print(d1)
# clear(), del
''


# * join 2 dictionary
# update()
d1 = {1:100, 2:200, 3:300, 4:400}
d2={"a":"apple", "b":"boy", "g":"game"}
d1.update(d2)
print(d1)

''
# get() -----> used to get the value from a key
d1 = {1:100,2:200,3:300,4:400}
# print(d1[90])
print(d1.get(90))
''
# to print all the keys
print(d1.keys())
print(type(d1.keys()))

# to print all the values
print(d1.values())

''





# *Iterating dictionary
for val in d1: # to iterate keys alone
   print(val)

# for val in dl.values():# to iterate values alone
   print(val)

# to get both key and values
# for key, val in d1.items():
print(key, val)

''
# ! problem:1

n = int(input("enter num of times:"))
integer=[]
float_value=[]
string=[]

for val in range(n):
    value = eval(input("enter the values:"))
    if type(value)==int:
        integer.append(value)
    elif type(value) == float:
            float_value.append(value)
    elif type(value)==str:
                string.append(value)
    else:
       print("pls provide data in int, float,string")
print(integer)
print(float_value)


''
# return a set of elements present in set A or B, but not both
# set1 = {10,20,30,40,50}
# set2 = {30,40,50,60,70}
# o/p
# {20,70,10,60}

set1 = {10,20,30,40,50}
set2 = {30,40,50,60,70}

for val in set1:
    if val not in set2:
        print(val)


for val in set2:
    if val not in set1:
        print(val)


for val in set1,set2:
  print(val)

# ! or
c = 0
for val in set1,set2:
    c=c+1
    if c==1:
        for element

'''
# ! -------> problem :3

l1 = [1,2,3,4,]# key
l2 = ["a","b","c","d"] # value

for val in range(len(l1)):
    d1[l1[val]] =l2[val]
    print(d1)
    




















# {1:'a'}

d1 = {}
d1[l1[0]] = l2[0]
print(d1)










