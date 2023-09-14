import requests
import sys
import tkinter as tk
from tkinter import messagebox
from bs4 import BeautifulSoup
from urllib.parse import urlparse

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

# 关键字
keyword_label = tk.Label(root, text="请输入关键词：")
keyword_label.grid(row=2, column=0, padx=10, pady=10)
keyword_var = tk.StringVar(value="")
keyword_entry = tk.Entry(root, textvariable=keyword_var)
keyword_entry.grid(row=2, column=1, padx=10, pady=10)


# 搜索结果输出
result_label = tk.Label(root, text="搜索结果：")
result_label.grid(row=6, column=0, padx=10, pady=10, columnspan=2)


# 筛选按钮
def filter():
    difficulty = difficulty_var.get()
    tiku = tiku_var.get()
    keyword = keyword_var.get()

    if difficulty=="全部": dit=None
    elif difficulty=="暂无评定": dit=0
    elif difficulty=="入门": dit=1
    elif difficulty=="普及-": dit=2
    elif difficulty=="普及/提高-": dit=3
    elif difficulty=="普及+/提高": dit=4
    elif difficulty=="提高+/省选-": dit=5
    elif difficulty=="省选/NOI-": dit=6
    elif difficulty=="NOI/NOI+/CTSC": dit=7

    if tiku=="洛谷": type="B%7CP"
    elif tiku=="主题库":type="P"
    elif tiku=="入门与面试":type="B"
    elif tiku=="CodeForces":type="CF"
    elif tiku=="SPOJ":type="SP"
    elif tiku=="AtCoder":type="AT"
    elif tiku=="UVA":type="UVA"

    response=requests.get(f"https://www.luogu.com.cn/problem/list?type={type}&difficulty={dit}&page={1}&keyword={keyword}",headers=headers)
    html=response.text
    txt=BeautifulSoup(html,features="lxml")

    for content in txt.find_all("a"):
        num=content.get("href")
        problem=content.string #题目
        
        if num=="P1000":
            in_response=requests.get(f"https://www.luogu.com.cn/problem/{num}",headers=headers)
            in_html=in_response.text
            in_txt=BeautifulSoup(in_html,features="lxml")
            print(in_txt)
            

    # TODO: 根据难度和关键字进行筛选算法
    result_label.config(text="搜索结果：难度:{} 题库:{} 关键字:{} ".format(difficulty,tiku,keyword)) 

        
filter_button = tk.Button(root, text="筛选", command=filter)
filter_button.grid(row=3, column=0, padx=10, pady=10)






# 启动主事件循环
root.mainloop()