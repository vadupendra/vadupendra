'''
# Code:
#d1 {'Ten': 10, 'Twenty': 20, 'Thirty': 30} #d2= {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
#d1.update(d2)
# print(d1)


#2.) Python Program to determine if
#the given Sets Are Disjoint # or Not without Using Inbuilt-in Functions

# set1 {'Python', 'Java', 'Data Science'}
#set2 = {'ML', 'AI', 'R Language', 'Python'}
# set = {data analytics,'robotics','deep learning'}



c = 0
flag=0
for val in range(3):
     C=C+1
     if c==1:
         for val in set1:
             if val in set2 or val in set3:
                 flag=1
                 break
     if c==2:
         for val in set2:
             if val in set1 or val in set3:
                 flag=1
                 break
     if c==3:
         for val in set3:
             if val in set2 or val in set1:
                 flag=1
                 break

# if flag==0
      print("disjiont")
# else:
      print("jiont")

''

#3.)
list1 = ["M", "па", "1", "Ke" ] 
list2 = ["y", "me", "s", "lly"]

       
# l3 =  []
# for val in range(len(listl)):
#    ans list1[val] (list2[val]
#    l3.append(ans)
# print(l3)
''
# i = 0
while i<len(list):
l3.append(list1[i]+list2[i])
    i+=1
print(l3)

''

# !    funtions
#? def
# funtion is a block of code

# ? function has 3 parts
# funtion declaration
# function defanition
# functional call

# ! eg:1
def greet(): # function defanition
    print("greeting user!!")

greet()
greet()
greet()
greet()
greet()
greet()
greet() # function calling

'''

# ! eg:2
def adding():
    a = 4
    b = 5
    c = 3
    d = a+b+c
    print(d)





      
