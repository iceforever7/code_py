import requests
import tkinter
from tkinter import messagebox
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import urllib.request,urllib.error
import bs4,re

import selenium,time,pyperclip,pyautogui,os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait



headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
    "Cookie":"login_referer=https%3A%2F%2Fwww.luogu.com.cn%2Fauth%2Flogin;_uid=667218;__client_id=74a5e8b36aa466ce90a9399a9c4004aa7bb6efc0;C3VK=0d19c2"
}
#防止404和跳过登录

response=requests.get("https://www.luogu.com.cn/problem/list?page=1",headers=headers)
html=response.text
txt=BeautifulSoup(html,features="lxml")
#获取page内容

Chrome=webdriver.Chrome()

for content in txt.find_all("a"):
    num=content.get("href")#编号
    problem=content.string#题名

    if num=="P1000" :
        
        """url_problem=(f"https://www.luogu.com.cn/problem/{num}")
        pyperclip.copy("")
        l=""
        Chrome.get(url_problem)
        WebDriverWait(Chrome,20)
        time.sleep(1)
        Chrome.find_element(By.XPATH,'//*[@id="app"]/div[2]/main/div/section[2]/section/div/div[1]/a[1]').click()
        if(pyperclip.paste()!=l):
            text = pyperclip.paste()
            file_path = f'C:\\Users\\Administrator\\Desktop\\题解\\{num}-{problem}.md'
            with open(file_path, 'w',encoding='utf-8') as f:f.write(text)"""
        #题目


        url_solutin=(f"https://www.luogu.com.cn/problem/solution/{num}")
        Chrome.get(url_solutin)
        

        solution= Chrome.find_elements_by_class_name("marked")
        for so in solution:
            print(so.text)

    
    
        
        
       
Chrome.quit()
#获取