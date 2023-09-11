# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 13:17:37 2020

@author: User
"""

#%%
import requests
from bs4 import BeautifulSoup
#import csv
from time import localtime, strftime
from os.path import exists
html = requests.get("https://rate.bot.com.tw/xrt?Lang=zh-TW")
bsObj = BeautifulSoup(html.content, "lxml")
for single_tr in bsObj.find("table", {"title":"牌告匯率"}).find("tbody").findAll("tr"):
    cell = single_tr.findAll("td")
    currency_name = cell[0].find("div", {"class":"visible-phone"}).contents[0]
    
    currency_name = currency_name.replace("\r", "")
    currency_name = currency_name.replace("\n", "")
    currency_name = currency_name.replace(" ", "")
    currency_rate = cell[2].contents[0]
    print(currency_name, currency_rate)
    file_name = "C:\\Users\\User\\Desktop\\bkt_rate"+currency_name+".csv"
    now_time = strftime("%Y-%m-%d %H:%M:%S", localtime())
    if not exists(file_name):
        data = [['時間', '匯率'], [now_time, currency_rate]]
    else:
        data = [[now_time, currency_rate]]
#    f = open(file_name, 'a')
#    w = csv.writer(f)
#    w.writerows(data)
#    f.close()
#%%

#$ pip install selenium
#
#$ pip install beautifulsoup4
#
#$ pip install webdriver-manager

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
import time
from os.path import exists
html = requests.get("https://mops.twse.com.tw/mops/web/t163sb15")
bsObj = BeautifulSoup(html.content, "lxml")
print(bsObj)

#%%

import pandas as pd
df = pd.read_html('http://isin.twse.com.tw/isin/C_public.jsp?strMode=2',
                  encoding='big5hkscs', header=0)
newdf=df[0][df[0]['產業別'] > '0']
del newdf['CFICode'], newdf['備註']
df2=newdf['有價證券代號及名稱'].str.split('　', expand=True)
df2 = df2.reset_index(drop=True)
newdf=newdf.reset_index(drop=True)
'''
for i in df2.index: 
    if '　' in df2.iat[i, 0]:
        df2.iat[i, 1]=df2.iat[i, 0].split('　')[1] # index at (iat) 
        df2.iat[i, 0]=df2.iat[i, 0].split('　')[0]
'''
newdf=df2.join(newdf)
newdf=newdf.rename(columns = {0:'股票代號', 1:'股票名稱'})
del newdf['有價證券代號及名稱']
newdf.to_excel('stock_list.xlsx', sheet_name='Sheet1', index=False)

#%%

import pandas as pd
ex_pandas = pd.Series([3, 6, 9, 12], index=['A','B','C','D'])
print(ex_pandas.values)
print(ex_pandas.index)
print(ex_pandas['B'])
print('D' in ex_pandas)

data = {'name':['Bob', 'Nancy'], 'year':[1996,1997], 'month':[8,1], 'day':[11,8]}
myframe = pd.DataFrame(data)
print(myframe)
print(myframe.head(1), myframe.tail(1))

print(myframe.info())
print(myframe.shape)

import pandas as pd
fn = "API_EG.ELC.NUCL.ZS_DS2_en_csv_v2_180676.csv"

df = pd.read_csv(fn, encoding='utf8')
df = df.fillna(0)
print(df.loc[0, 'Country Name'])

print(df.iloc[0:2,:])

sector = df.groupby("Country Name")
print(sector)
print(sector.size())
print(sector.get_group("American Samoa"))
print(df)
tit = df.iloc[7:9, 55:59]
mask = tit["2014"] > 0
print(tit[mask])

