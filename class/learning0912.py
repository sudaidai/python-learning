# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#%%

print("Hello World!!")

#%%

num1 = 19 #number
num2 = 89 #number
not_exist_number = "64" #string

print(num1 + num2) 
#print(num1 + num2 + not_exist_number) (get error, integer can not add by string)
print(num1 + num2, not_exist_number)
print(num1 + num2 + eval(not_exist_number)) #eval() turns string to number

# HW1: In the code above, how to print out 198964 by those three variables?

#%%

bruce = "Bruce"
where_is_my_money = 87

hytech = "海科🚀"
score = 87.8787878787

IQ = 180


# Let's give bruce $87
print("%s存款剩%d元" % (bruce, where_is_my_money))

# Hytech on the way
print("%s未來無可限量! 評審請給分:%.12f" % (hytech, score))

# The IQ of IQs
print("IQ%5d" %IQ)

# HW2: In the code above, how to print out 87海科(ya! rocket is on the way)87.8787

#%%

list_1 = [1,2,3,4,5]
list_2 = [6,7,8,9,10]
list_3 = list_1 + list_2

print(list_3)

lst = list(range(0, 10))
print(lst)

# HW3: How to print out [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] using range?

#%%

"""
What if we would like to print the message below?
*
**
***
****
*****
******
*******
********
*********
**********
"""

n = eval(input("請問要從1印到?"))

print("range:", end=' ')
for number in range(0, 10):
    print(number+1, end=' ')
    
print()

print("list3:", end=' ')
for number in list_3:
    print(number, end=' ')

for number in range(10):
    for number2 in range(number):
        print('*', end='')
    print()

for number in range(10):
    for number2 in range(10-number):
        print('*', end='')
    print()

for number in range(10, 0, -1):
    for number2 in range(number):
        print('*', end='')
    print()

#%%

print(1 == 2)
print(2 == 2)
print(True and False)
print(True or False)
print(not True)
print(not(True or False))
print(1 >= 3)
print(1 < 3)
print(1 != 3)

# Aha! No homework

#%%

import random
a = random.randint(1, 314159)

print(random.random())
print(random.random())
print(random.random())
print(random.random())
print(random.random())
x=[1, 2, 5, 7, 9]

random.shuffle(x)
print(x)

# Aha! No homework, but it would use next time!

#%%

print()

print("hello world!!")
print(8, "hello", 8)
print()
print(8, "hello", 8, sep="&")

print()
username="海科"
score=100
print("%s的分數為%d" %(username, score))

print()
price=3.1415
print("price:%2.9f" %price)

# Aha! No homework

#%%

x=30
print("x=/%-6d/" %x)

y=12.5
print("y=/%-7.2f/" %y)

string="deep"
print("s=/%-6s/" %string)

x=50
print("x=/%+6d/" %x)
y=15.1
print("y=/%+6.2f/" %y)

# Aha! No homework

#%%

print()
print(ord('B')) # Unicode code point of the character 'B'
print(ord('&'))
print(chr(67)) # Convert the integer 67 into its corresponding character. In Unicode, 67 represents the character 'C
print(chr(8365))
print(len("this is my python program"))
print(max("this is my python program"))
print(min("this is my python program"))
print("from" in "information")
print("python" in "information")
print("from" not in "information")

s="Today is a beautiful day"

print(s.upper())
print(s.lower())
print(s.swapcase())
print(s.replace("beautiful", "sunny"))
print(str.capitalize("python"))
print(str.title("a book"))

# HW4: Does "form in information" would be true or false? Why?

#%%

print()
print(str.isalpha("apple888"))
print(str.isalpha("sudaidai")) # All of it is alphabet
print(str.isdigit("1999"))     # All of it is number
print(str.isdigit("1999ssss"))
print(str.isalnum("8888.1999"))# Except float
print(str.isalnum("su1212"))   # All of it is alpabet or number"
print(str.isupper("su"))
print(str.isupper("SU"))
print(str.islower("su"))
print(str.islower("SU"))

# HW5: Does "sudaidai1212" would be true or false for "isalpha", "isalpha", "isalnum", "isupper", "islower"?

#%%

print()
s="sususususususu"
print(s.count("su"))
print(s.startswith("su"))
print(s.startswith("s"))
print(s.endswith("su"))
print(s.endswith("s"))
print(s.find("su"))
print(s.rfind("su"))

# Aha! No homework

#%%

print()
s="            SU       "
print(s.strip())
print(s.lstrip())
print(s.rstrip())

x="www.google.com"
print(x.strip("cmowz"))
print(x.lstrip("cmowz"))
print(x.rstrip("cmowz"))

# Aha! No homework

#%%

print()
s="Hello World!"
print(s.center(20, '#'))
print(s.ljust(20, '♥'))
print(s.rjust(20, '♧'))
print("-100".zfill(6))

# Aha! No homework

#%%

print()
print(format(168, "<10"))
print(format(168, ">10"))
print(format(168, "^10"))
print(format(168, "@^10"))
print(format(1234567890, ","))
print(format(65, "#b"))
print(format(65, "#o"))
print(format(65, "#x"))
print(format(168, "+010"))
             
# Aha! No homework
             
#%%

"""
HW6: Given a user input n(ex:9), print out the diamond below
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *

1. How to print out this?
    *
   ***
  *****
 *******
*********

2. How to print out this?
*********
 *******
  *****
   ***
    *
"""
