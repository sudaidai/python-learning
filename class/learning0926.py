# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 23:23:42 2020

@author: bruce
"""

#%%

class Dog():
    def __init__(self, name, age):
        # 設定物件本身(self)屬性(.name/age)為外部參數(name/age)
        self.name = name
        self.age = age
    
    # 叫的方法
    def bark(self, times=1):
        return "汪" * times
    
    # 利用 @property，將方法設定為屬性
    # 你可以看到物件裡面，內部參數的傳遞都是靠self來傳
    @property
    def asHumanAge(self):
        return self.age * 7
        
park = Dog("Park", 3)
print(park.name)
print(park.age)
print(park.bark(3))
print(park.asHumanAge)
# 檢查park這個實例裡面，含有什麼屬性和方法
print(dir(park))

#%%

try:
    a = int(input())
    b = int(input())
    print(a/b)
except ZeroDivisionError:
    print("Cannot divide by 0!")
except:
    print("Wrong input")
    
#%%

#回頭看串列(list)

lst = ["black", "yoyo", "dai"]
print(lst[-1])
lst.append("passerby")
print(lst[0:3])
print(lst[:3])
print(lst[2:])
lst.insert(2, "passerby")
print(lst)

lstPassersby = ["passerby1", "passerby2", "passerby3"]
lst.extend(lstPassersby)
print(lst)

lst.remove("passerby")
print(lst)

for i in range(4):
    popped = lst.pop()
    print(popped + "(QQ)")

print(lst)

lstHash = lst + lstPassersby
print(lstHash)

lst.sort()
print(lst)
lst = [5, 4, 8, 7]
lst.sort()
print(lst)

lst.sort(reverse=True)
print(lst)

sorted_list = sorted(lst)
print("sorted_list: ", sorted_list, "\nlst: ", lst, sep='')

print(max(lst))
print(sum(lst))
print(min(lst))

print(lst.index(8))

for index, num in enumerate(lst, start=0):
    print(index, num)

lst = input().split()
print(lst)

#%%

#list comprehension

count = [i for i in range(1, 11)]
square = [i*i for i in range(1, 11)]
print(count, '\n', square, sep='')

sentence = "the rocket came back from mars"
vowels = [i for i in sentence if i in "aeiou"]
print(vowels)

#set&dict's comprehesion is the same

