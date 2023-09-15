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


print(txt.text)

        
        
"""
        time.sleep(30)
        Chrome.get(url_solutin)
        cookie= Chrome.get_cookies()
        print(cookie)
        #获取登录cookie"""

#获取