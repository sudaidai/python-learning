# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 19:03:45 2020

@author: sudaidai
"""

#%%

'''
將list存成csv
'''

lst = [1,3,4,5,6,7,7,8]

f = open("test.csv", 'w')

words = str(lst)
words = words.lstrip('[')
words = words.rstrip(']')
print(words)

f.write(words)
f.close()

#%%

from selenium import webdriver

url = "https://www.fju.edu.tw/"
driver = webdriver.Chrome()
driver.get(url)

btn = driver.find_element_by_link_text("教職員工")
btn.click()
#%%

import pandas as pd

dic = {
    "col 1": [1, 2, 3], 
    "col 2": [10, 20, 30],
    "col 3": list('xyz'),
    "col 4": ['a', 'b', 'c'],
    "col 5": pd.Series(range(3))
}

df = pd.DataFrame(dic)
print(df)

df.columns = ["new1", "NEW2"] + list(df.columns[2:])
print(df)

#%%

import pandas as pd

# 你可以用類似的方式爬取任何網路上的公開數據集 這幾行別看
base_url = "https://data.taipei/api/getDatasetInfo/downloadResource?id={}&rid={}"
_id = "2f238b4f-1b27-4085-93e9-d684ef0e2735"
rid = "ea731a84-e4a1-4523-b981-b733beddbc1f"
csv_url = base_url.format(_id, rid)
df_raw = pd.read_csv(csv_url, encoding='big5')

# 複製一份做處理
df = df_raw.copy()

# 計算不同區不同性別的死亡、受傷人數
df['區序'] = df['區序'].apply(lambda x: ''.join([i for i in x if not i.isdigit()]))
df = (df[df['性別'].isin([1, 2])]
      .groupby(['區序', '性別'])[['死亡人數', '受傷人數']]
      .sum()
      .reset_index()
      .sort_values('受傷人數'))

df['性別'] = df['性別'].apply(lambda x: '男性' if x == 1 else '女性')
df = df.reset_index().drop('index', axis=1)
df.to_csv("Analytic01.csv", encoding='utf8')
print(df_raw.head())
print(df.head())

#%%

driver.quit()