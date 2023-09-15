import requests
import tkinter
from tkinter import messagebox
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import urllib.request,urllib.error
import bs4,re
import scrapy
from scrapy.http  import  Request,FormRequest
import selenium,time,pyperclip,pyautogui,os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import html2text
import os


headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
    "Cookie":"c"
}
#防止404和跳过登录

responses=requests.get("https://www.luogu.com.cn/problem/list?page=1",headers=headers)
html=responses.text
txt=BeautifulSoup(html,features="lxml")
#获取page内容



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

        Chrome= webdriver.Chrome()
        url_solutin=(f"https://www.luogu.com.cn/problem/solution/{num}")
        Chrome.get(url_solutin)
        new_cookie =  {'domain': 'www.luogu.com.cn', 'expiry': 1694747291, 'httpOnly': False, 'name': 'C3VK', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'e3c0b2'}
        Chrome.add_cookie(new_cookie)
        new_cookie = {'domain': '.luogu.com.cn', 'expiry': 1697338993, 'httpOnly': True, 'name': '_uid', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': '667218'}
        Chrome.add_cookie(new_cookie)
        new_cookie = {'domain': '.luogu.com.cn', 'expiry': 1697338975, 'httpOnly': True, 'name': '__client_id', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': '4c5dcd654c6e51204df13357faf7401edb5f7f3a'}
        Chrome.add_cookie(new_cookie)
        Chrome.get(url_solutin)
        ele=Chrome.page_source
        in_txt=BeautifulSoup(ele,features="lxml")
        print(in_txt.find("marked"))
        #file_path = f'c:\\Users\\尘\\Desktop\\题解\\tijie.md'
        #with open(file_path, 'w',encoding='utf-8') as f:f.write()
        time.sleep(5)
        
        
        """
        time.sleep(30)
        Chrome.get(url_solutin)
        cookie= Chrome.get_cookies()
        print(cookie)
        #获取登录cookie"""

        
Chrome.quit()
#获取