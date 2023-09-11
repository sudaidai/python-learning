# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 12:53:58 2020

@author: bruce
"""

#%%
path = "C:\\Users\\bruce\\OneDrive\\Documents\\pyLearn\\class\\file_hello.txt"
# f = open(path, 'r')
f = open(path)
words = f.read()
print(words)
f.close()

#%%

path = "C:\\Users\\bruce\\OneDrive\\Documents\\pyLearn\\class\\create.txt"
f = open(path, 'w')
f.write("HaHaHa")
f.close()

#%%

from pathlib import Path

f = Path("C:\\Users\\bruce\\OneDrive\\Documents\\pyLearn\\class\\file_hello.txt")
f1 = Path("C:\\Users\\bruce\\OneDrive\\Documents\\pyLearn\\class\\file_hello1.txt")
print(f.stat())
print(f1.stat())

#%%

path = "C:\\Users\\bruce\\OneDrive\\Documents\\pyLearn\\class\\create.txt"
f = open(path, 'a')
f.write("HaHaHa")
f.close()

#%%

path = "file_hello.txt"
with open(path, 'r') as f:
    # word = f.read()
    # print(word)
    print(f.readline())

