'''
# 1.) python program to capitalize the first and last character of each
# word in a string
s1 = amma,nanna
print(s1.capitalize())
print(s1)
''
s1 = input("upendra star")
fst = s1[0].upper()
lst = s1[1].upper()
print(fst+s1[1:len(s1)-1]+(lst))

''
# 2.) input : 128
# output : yes

n = 128
temp = n
f1 = 0
while n!=0:
    rem = n%10
    check= tem % rem
    if check!=0:
        f1 = 1
    n = n//10
    


if f1==0:
    print("yes")
else:
    ptint("no")



''
l1 = [2,4,6,6,8]
l2 = [7,8,6,5,4]
l3 =[]
for val in range(len(l1)):
    ans = l1[val]+l2[val]
    l3.append(ans)
print(l3)
''
# !-------> set

# ? charctristics of set
# 1.) set can be treated using {}
# 2.) the elements inside set are not indexed
# 3.) does not allow duplicate values
# 4.) it unordered
# 5.) heterogenous
# 6.) mutable or changable

# eg:1
s1 = {9,9,89,7,76,8+7j,(8,7,5), "truck", 'e'}
print(s1)

''
# eg:2
s2 = {5,8,98,[9,0]}
print(s2) ---> error

''
# * eg:3
min(), max(), len()
''
# * eg:4
s1 = {8,78,67,'u'}
add()
s1.add(43)
print(s1)

''
# ? to delete element inside set
s1 = {8,78,67,'u'}
print(s1)
''

pop() # to delete one element randomly
s1.pop()
print(s1)
'''

#isdisjoit(), issubset(), issuperset()
s1={8, 9, 0}
s2= (6, 7, 5, 8, 9, 0)
print(s1.issubset(s2))
print(s2.issuperset (s1))





