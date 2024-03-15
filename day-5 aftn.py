# ! -------> strings
'''

s1 = 'o'
print(type(s1))

s1 = "u"
print(type(s1))

s1 = "hello world"
# * to access string
print(s1)
# indexing and slicing ---> same as list and tuple
s1 = 'hello world'
print(s1[0:5])
''
# ----> common funtions

# len(), min(),max(), index(),count()
s1 = "hello world"
print(len(s1))
print(max(s1))
print(min(s1))
''
# ord()----> used to find the ASCII value of a character
s1 = "u"
print(ord(s1))

# funtions of string
s1 = " hello world"
''

# ? to convert all character to upper case
print(s1.upper()
''

# ? to convert to lower case
s1 = "jnngjnj"
print(s1.lower())
''

# strip()  --> to eliminate the space in begining and end of string
s1 = " where are you?"
print(s1.lstrip())
print(s1.rstrip())
print(s1.strip())
''
# split() ----> to split the words  in srting based on a character
s1 = "where are you?"
print(s1.split())
print(sl.split("r"))

print(s1.count('e'))

''
# * replace() --> to replace a specific char in the string
s1 = "whetre are you?"
print(s1.replace('r', '&&'))
''
# * swapcase() ---> to convert to small and small to capital at a time
s1 = " hey there"
print(s1.swapcase())

''
# * title() --->to write the string in format of title
s1 = "never give up"
print(s1.title())

''
# * capitalize()-----> lst char of string will be converted to capital
s1 = "never give up"
print(s1.capitalize())

''
# * jion the strings
s1 = "hello"
s2 = 'world'
print(s1+s2)

s1 = ''how are you
iam fine
hey there
 ''
# * splilines() ---> used to split the string based on lines
print(s1.splitlines())
''
# * find() ---> to find the index based on a character
s1 = "hello world"
print(s1.find('z'))
print(s1.index('z'))
''
# * jion()--->
# l1 = ["hey","there"]
print(" ".jion(l1))
print("$".jion(l1))
''
s1 = "welcome to all"
# * print(s1.endswith('1))
# * print(s1.startswith('w'))

s1 = "67"
print(type(s1))
print(s1.isdigit())

''
# * print the string  in reverse manner
s1 = " welcome to all"
print(s1[::-1])
''''''
# ! ----> eg:1
# wap to find the number of lower case letters

s1 = " hey there you are"
for i in s1:
    if i.islower():
        count+=1
        print("the total num of lower case letters: ",count)


''
# ! eg:3
s1 = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
characters = len(s1)
print(characters)

words = s1.split(" ")
print(len(words))

sentences = s1.split('.')
for val in sentenses:
    if val =='':
        index = sentenses.index('')
        sentenses.pop(index)
print(len(sentenses))
'''
space = 0
for val in s1:
    if val ==" ":
        space=space+1
print(space)












