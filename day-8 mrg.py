'''
# ! eg:3
def profile(name,age,place):
    txt = "my name is{}.iam{}years old.iam from{}."
    print(txt.format(name,age,place))
profile("upi",20,"abc")   
''
# eg:4
# ? function with return statement



#! return
#1.) A variable declared inside the function can be accessed outside the function #using return
# using return
#2.) return does not prrint anything
#3.) we cannot write any code below return statement




def f1(a,b):
    c=a*b
    return c
# print(f1(7,5))
obj = f1(7,5)
obj1 = f1(4,6)


def gracemark(object):
    print(object+4)
gracemark(obj)
gracemark(obj1)
''

def f1(a,b,c):
    c=a*b*c
print(f1(5,6,7))
obj = f1(5,6,7)
obj1 = f1(2,5,9)


def gracemark(object):
    print(object+8)
gracemark(obj)
gracemark(obj1)

''
#123
def palindrome(n):
    string = str(n)
    rev = str(n)[::-1]
    if string==rev:
        print(n,"palindrome")
    else:
        print("not palindrome")
a = int(input("enter the value"))
palindrome(a)

''
# ? based on the declaration of parameter and args
# ? funtions are devided into 5 categories

# positional
# keyword args
# default args
# variable length args
# keyword variable length args

# * positional args
# eg:1
def profile(name,phone,mark):
    txt = "my name is {}. my phone number is {}. i got {} marks."
    print(txt.format(name,phone,mark))


profile(9398360699,"upi",99) # unexpected output

''
# todo ----> exception of keyword args funtion
def profile(name,phone,mark):
    txt = "my name is {}. my phone number is {}. i got {} marks."
    print(txt.format(name,phone,mark))

# profile(name="uppi", phone= 9632587432 ,marks=99)# error->positional arsg follow keywordsdargs
# profile(9632587432, name="uppi" , mark=99) # error---> name has multiple values
profile("uppi",mark=99, phone=9632587432)

''
# * default args
# The method of assigning the argument to the paremeter while declaring the #functoin

# | Eg:1
def profile(name, phone, place="Kadapa"):
    txt = "My name is {}. My phone number is }. I am from {}."
    print(txt.format(name, phone, place))

profile("sid", 8767676767)

''

# ! eg:2
def profile(name, phone, place = "kadapa"):
    txt = "My name is {}. My phone number is {}. I am from {}."
    print(txt.format(name, phone, place))

profile("sid", 8767676767, "Guntur")

''

# ! Eg:2
def profile(name, phone, place="Kadapa"):
    if place == "Kadapa" or place=="KADPA" or place=="kadap":
       txt = "My name is {}. My phone number is {}. I am from {}."
       print(txt.format(name, phone, place))
    else:
       print("You are not eligible to Signup")
profile("sid", 8767676767)

''

Exception
def profile(name, place="KADAPA", phone); # error--> coz default args should not follow
                                          # positional param
    if place == "Kadapa" or place="KADAPA" or place == "kadapa":
       txt = "My name is {}. My phone number is {}. I am from {}."
       print(txt.format(name, phone, place))
    else:
       print("You are not eligible to Signup")
profile("sid", 8767676767)

'''





# * Variable length params
# Eg:1
# To pass more then 1 arg to a paremeter means we use variable length args.
# To convert normal paremeter to variable length param, add to ther prefix of param

# name = "sid", 'name2', 'name3'
def profile(*name):
     for val in name:
         print("My name is", val)
profile("sid", 'name2', 'name3')





















