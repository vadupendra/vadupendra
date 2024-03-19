'''
# ! Eg:0
def profile(*name,age):
    for val in name:
        print("my name is",val,"my age is",age)
profile("sid",'name2','name3',28) # error-----> age has args''

def profile(age,*name):
    for val in name:
        print("my name is",val,"my age is",age)
profile(28,"sid",'name2','name3')

''
# * keyword variable length args
# ! Eg:1

def price(**price_list):
    print(price_list)

price(shirt=1000, iphone=80000)

d1 = {"a":100,"b":200,"c":300}
d1 = dict(a=100, b=200, c=300)
print(d1)


''
# n = 5
# {1:1,2:4,3:9,4:16,5:25}

n = int(input("enter the number: "))
d1 = {}
for val in range(1,n+1):
    d1[val] = val**2
    print(d1)
''
def dict1(n):
    d1 = {}
    for val in range(1,n+1):
        d1[val] = val**2
    print(d1)
dict1(5)
''
# ! -----------> object oriented programming
the paradigms of objects oriented pprogramming are

# clas
# objects
# inheritance
# polymorphism
# abstraction
# encapsulation
''
# ! class is a blue print of an object
# l1 = [1,2,3,4,5,6]

# ? Eg:1
class c1:
    name1 = "sidhu"
    print(name1)
''
# ? Eg:2
class person:
    name = "sidhu"

c = person()
print(c.name)

''
# ? Eg:3
# create of a method
# when the function is created with a class is called as method

class person:
    def display(person): # it is a method
        print("hello wecome to classes")

p = person()
p.display()
''
#! Eg:4
# ! method with parameter
class person:
    def display(person,name,age):
        print(name,age)

p = person()
p.display("sidhu",28)

''
# ? Eg:5
class person1:
    fname = "sidhu" #attribute or static variable
    lname = "T"
    
    def first_name(self):
        print(self.fname)

    def full_name(self):
        print(self.fname+" "+self.lname)

p = person1()
p.first_name()
p.full_name()
'''
# ? Eg:6
# constructors ---->_init_()
# this is special method which has the ability to execute iotself without
# calling it manually through the process of instantiation

 class profile:
      def_init_(self): # constructor method
         print("darling")





    
