import requests
import tkinter
from tkinter import messagebox
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import urllib.request,urllib.error
import bs4,re

savePath = "C:\\Users\\Administrator\\Desktop\\题解\\"
#保存路径

headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
    "Cookie":"login_referer=https%3A%2F%2Fwww.luogu.com.cn%2Fauth%2Flogin;_uid=667218;__client_id=74a5e8b36aa466ce90a9399a9c4004aa7bb6efc0;C3VK=0d19c2"
}
#防止404和跳过登录

def getHTML(url):
    request = urllib.request.Request(url = url,headers = headers)
    response = urllib.request.urlopen(request)
    html = response.read().decode('utf-8')
    return html#获取页面

def getMD(html):
    bs = bs4.BeautifulSoup(html,"html.parser")
    core = bs.select("article")[0]
    md = str(core)
    md = re.sub("<h1>","# ",md)
    md = re.sub("<h2>","## ",md)
    md = re.sub("<h3>","#### ",md)
    md = re.sub("</?[a-zA-Z]+[^<>]*>","",md)
    return md#修改格式

def saveData(data,filename):
    cfilename = savePath + filename
    file = open(cfilename,"w",encoding="utf-8")
    for d in data:
        file.writelines(d)
    file.close()#保存文件


response=requests.get("https://www.luogu.com.cn/problem/list?page=1",headers=headers)
html=response.text
txt=BeautifulSoup(html,features="lxml")
#获取page内容


for content in txt.find_all("a"):
    num=content.get("href")#编号
    problem=content.string#题名

    if "P" in num :
        url_problem=(f"https://www.luogu.com.cn/problem/{num}")
        url_solutin=(f"https://www.luogu.com.cn/problem/solution/{num}")

        in_problem=requests.get(url_problem,headers=headers).text#题目
        in_solution=requests.get(url_solutin,headers=headers).text#题解

        print("正在爬取{}".format(num))
        in_html = getHTML(url_problem)
        problemMD = getMD(in_html)
        saveData(problemMD,num+"-"+problem+".md")
        print("爬取完毕")#题目导出
        
        
    
#获取