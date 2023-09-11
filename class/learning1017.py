# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 14:30:20 2020

@author: User
"""

#%%
from selenium import webdriver

url = "https://www.facebook.com"

email = ""
password = ""
driver = webdriver.Chrome()
driver.get(url)

driver.find_element_by_id("email").send_keys(email)
driver.find_element_by_id("pass").send_keys(password)
driver.find_element_by_id("u_0_b").click()

#driver.quit()

#%%

from selenium import webdriver
from bs4 import BeautifulSoup
import time

url = "https://mops.twse.com.tw/mops/web/t163sb15"
co_id = "2498"

driver = webdriver.Chrome()
driver.get(url)

driver.find_element_by_id("co_id").send_keys(co_id)
search_btn = driver.find_element_by_css_selector\
("#search_bar1 > div > input[type=button]")
search_btn.click()

time.sleep(3)
bsObj = BeautifulSoup(driver.page_source, "lxml")

#%%

driver.quit()