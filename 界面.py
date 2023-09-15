import requests
import tkinter as tk
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

#防止404
headers={
    "User-Agent":
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}

# 创建主窗口
root = tk.Tk()
root.title("题目筛选器")
root.geometry("960x540+500+150")

# 题目难度
difficulty_label = tk.Label(root, text="请选择题目难度：")
difficulty_label.grid(row=0, column=0, padx=10, pady=10)
difficulty_var = tk.StringVar(value="全部")
difficulty_options = ["全部","暂无评定","入门","普及-","普及/提高-","普及+/提高","提高+/省选-","省选/NOI-","NOI/NOI+/CTSC"]
difficulty_menu = tk.OptionMenu(root, difficulty_var, *difficulty_options)
difficulty_menu.grid(row=0, column=1, padx=10, pady=10)

#题库
tiku_label = tk.Label(root, text="请选择所属题库：")
tiku_label.grid(row=1, column=0, padx=10, pady=10)
tiku_var = tk.StringVar(value="洛谷")
tiku_options = ["洛谷","主题库","入门与面试","CodeForces","SPOJ","AtCoder","UVA"]
tiku_menu = tk.OptionMenu(root, tiku_var, *tiku_options)
tiku_menu.grid(row=1, column=1, padx=10, pady=10)

#爬取题数
num_label = tk.Label(root, text="请输入题目数:")
num_label.grid(row=2, column=0, padx=10, pady=10)
num_var = tk.StringVar(value="")
num_entry = tk.Entry(root, textvariable=num_var)
num_entry.grid(row=2, column=1, padx=10, pady=10)

# 关键字
keyword_label = tk.Label(root, text="请输入关键词：")
keyword_label.grid(row=3, column=0, padx=10, pady=10)
keyword_var = tk.StringVar(value="")
keyword_entry = tk.Entry(root, textvariable=keyword_var)
keyword_entry.grid(row=3, column=1, padx=10, pady=10)


# 搜索结果输出
result_label = tk.Label(root, text="搜索结果：")
result_label.grid(row=6, column=0, padx=10, pady=10, columnspan=2)


# 筛选按钮
def filter():

    global dit,ty,keyword
    #获取键值
    difficulty = difficulty_var.get()
    tiku = tiku_var.get()
    keyword = keyword_var.get()

    #难度选择
    if difficulty=="全部": dit=None
    elif difficulty=="暂无评定": dit=0
    elif difficulty=="入门": dit=1
    elif difficulty=="普及-": dit=2
    elif difficulty=="普及/提高-": dit=3
    elif difficulty=="普及+/提高": dit=4
    elif difficulty=="提高+/省选-": dit=5
    elif difficulty=="省选/NOI-": dit=6
    elif difficulty=="NOI/NOI+/CTSC": dit=7

    #题库选择
    if tiku=="洛谷": ty="B%7CP"
    elif tiku=="主题库":ty="P"
    elif tiku=="入门与面试":ty="B"
    elif tiku=="CodeForces":ty="CF"
    elif tiku=="SPOJ":ty="SP"
    elif tiku=="AtCoder":ty="AT"
    elif tiku=="UVA":ty="UVA"
    

    # TODO: 根据难度和关键字进行筛选算法
    #result_label.config(text="搜索结果：难度:{} 题库:{} 关键字:{} ".format(difficulty,tiku,keyword)) 

filter_button = tk.Button(root, text="筛选", command=filter)
filter_button.grid(row=5, column=0, padx=10, pady=10)

def run_or_die():
    #解析题库页
    allnum=num_var.get()
    if allnum=="": allnum="1"
    nums=int(float(allnum))
    print(nums)
    pagenum=nums//50
    pagenum=pagenum+2
    print(pagenum)

    chrome_options =webdriver.ChromeOptions()
    chrome_options.headless = True
    for i in range(1,pagenum):
        print(i)
        responses=requests.get(f"https://www.luogu.com.cn/problem/list?type={ty}&difficulty={dit}&page={i}&keyword={keyword}",headers=headers)
        html=responses.text
        txt=BeautifulSoup(html,features="lxml")
        print("running")
        for content in txt.find_all("a"):
            num=content.get("href")#编号
            problem=content.string#题名

            if '?' not in num :

                nums=nums-1
                if nums <0:
                    break
                else:

                    Chrome= webdriver.Chrome()
                    Chrome.minimize_window()
                    path=f"C:\\Users\\Administrator\\Desktop\\题解\\{dit}-{keyword}\\{num}-{problem}"
                
                    if not os.path.exists(path):
                        os.makedirs(path)

                    url_problem=(f"https://www.luogu.com.cn/problem/{num}")
                    pyperclip.copy("")
                    l=""
                    Chrome.get(url_problem)
                    WebDriverWait(Chrome,20)
                    time.sleep(1)
                    Chrome.find_element(By.XPATH,'//*[@id="app"]/div[2]/main/div/section[2]/section/div/div[1]/a[1]').click()
                    if(pyperclip.paste()!=l):
                        text = pyperclip.paste()
                        with open(os.path.join(path,f"{num}-{problem}.md"), 'w',encoding='utf-8') as f:f.write(text)
                    #题目

                    
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
                    in_txt=BeautifulSoup(ele,"html.parser")
                    md=in_txt.find(class_="solution-article")
                    if md==None:continue
                    m="<h1>"+md.prettify()
                    markdown=html2text.html2text(m)
                    with open(os.path.join(path,f"{num}-{problem}-题解.md"), 'w',encoding='utf-8') as f:f.write(markdown)
                    #题解

                    time.sleep(5)
                    
                    
            
                """ time.sleep(30)
                    Chrome.get(url_solutin)
                    cookie= Chrome.get_cookies()
                    print(cookie)
                    #获取登录cookie"""

                
            Chrome.quit()
     
run_button = tk.Button(root,text="崩溃",command=run_or_die)
run_button.grid(row=6,column=0,padx=10,pady=10)

# 启动主事件循环
root.mainloop()