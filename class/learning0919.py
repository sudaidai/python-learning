# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 21:52:08 2020

@author: User
"""

#%%
'''
判斷輸入的數值是否大於0 如果大於0則輸出訊息:
您輸入的數值  大於0
無論是否大於0. 最後皆輸出結束
'''

print()
num = eval(input("Please enter a value:"))

if (num > 0) :
    print("the value", num , "is greater than 0")
    
print("end")

#%%
    
#輸入任意數值，判斷該數值為奇數或偶數
print()
num = eval(input("please enter an integer:"))

print(9%2)

if (num % 2==0) :
    print("even")
else:
    print("odd")

#%%p

n = eval(input("輸入一個數字:"))

if(n>9):
    print("n>9")
elif(n>3 and n<=9):
    print("3<n<=9")
else:
    print("n<=3")

#%%

#巢狀if

print()
score = eval(input("enter ur score:"))

if score>=90:
    print("優")
else:
    if score>=80:
        print("甲")
    else:
        if score>=70:
            print("乙")
        else:
            if score>=60:
                print("丙")
            else:
                print("fail")

#%%
'''
西元年份除以4可以整除且除以100不可整除或西元年分除以400可以整除為閏年
'''

print()
year = eval(input("Please enter the year:"))
if (year%4==0 and year%100!=0) or (year%400==0):
    print("leap year")
else:
    print("not leap year")

#%%
print()
x=eval(input("compute the factorial of x, enter an integer x:"))
total=1
i=1
while i<=x:
     total = total*i
     i+=1
print(total)

#%%

print()
total = num = score =0
while score!=-1:
    num+=1
    total = total + score
    score = eval(input("請輸入第%d位學生的成績(輸入-1結束):" % num))
    
average = total / (num-1)
print("總分為", total, "平均為%5.2f" % average)

#%%

def Fib(N):
    if N==0:
        return 0
    elif N==1:
        return 1
    else:
        return Fib(N-1) +Fib(N-2)  
for i in range(10):
    print(Fib(i), end=' ')

#%%

import random
lotto =[]
n=1
while n<=6:
    randNum = random.randint(1, 49)
    if randNum not in lotto:
        lotto.append(randNum)
        n+=1
print("樂透號碼是: \n", end='')
for i in lotto:
    print("%3d" %i, end='')
print()

lotto.sort()
print("號碼排序後:")
for i in lotto:
    print("%3d" %i, end='')
print()

#%%

#Tuple
num =(10,20,30,40,50)
fruits=('apple', 'orange', 'banana')
val_tuple=(100, )
print(num[0])
print(num[4])
print(fruits[1])
print(val_tuple[0])
for i in num:
    print(i)
    
#%%
hexChar = input()
hexChar = hexChar.upper()
if hexChar >='0' and hexChar<='9':
    print(ord(hexChar)-ord('0'))
elif hexChar >='A' and hexChar <='F':
    print(ord(hexChar)-ord('A')+10)
else:
    print("error")
#%%
    
#Set
    
print()

math = {'Kevin','Kevin', 'Peter', 'Eric'}
math.add('trin')
physics = {'Peter', 'Nelson', 'Tom'}
both = math & physics

print("同時參加數學與物理夏令營的成員", both)
print(math | physics) #有參加
print(math - physics) #只參加數學
print(math ^ physics) #有參加但沒有都參加

#%%

#Dict

fruits = {'西瓜':20, '香蕉':10, '水蜜桃':25}
noodles = {'牛肉麵':100, '肉絲麵':80, '陽春麵':60}
print("水蜜桃一斤 = ", fruits['水蜜桃'], "元")
print("牛肉麵一碗 = ", noodles['牛肉麵'], "元")

#add to dict
fruits['橘子'] = 17
print(fruits)
print("橘子一斤 = ", fruits['橘子'], "元")

for fruit, price in fruits.items():
    print("\n水果", fruit)
    print("價格", price)
    
print(tuple(fruits.keys()))

print(fruits.get('香蕉', "error"))

#%%
players = {'Stephen Curry':'Golden State Warriors', 
           'Kevin Durant':'Golden State Warriors', 
           'Lebron James':'Cleveland Cavaliers'}

for name in sorted(players.keys()):
    print(name)
    print("Hi, %s I like ur performance in %s" %(name, players[name]))
    
#%%
    
sports = {'Curry':['籃球', '美式足球'], 
          'James':['football', 'baseball', 'basketball']}

for name , Psports in sports.items():
    print("%s喜歡的運動是:" %name)
    for sport in Psports:
        print(" ", sport)
        
#%%
        
wechat_account = {'cshung':{'name':'李大年', 
                            'city':'台北'}, 
                  'kevin':{'name':'王大同', 
                           'city':'北京'}
                  }
for account, account_info in wechat_account.items():
    print("user name = ", account)
    print("name      = ", account_info['name'])
    print("city      = ", account_info['city'])

#%%
    
survey_dict = {}
market_survey = True
while market_survey:
    name = input("\nPlease enter ur name : ")
    travel_location = input("Enter ur fantastic tourist attraction : ")
    survey_dict[name] = travel_location
    repeat = input("Is anyone continuing?(y/n) ")
    if repeat != 'y':
        market_survey = False
print(survey_dict)
print("\nThere's result")
for user, location in survey_dict.items():
    print(user, "Tourist attraction: ", location)