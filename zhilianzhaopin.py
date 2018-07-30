#主要逻辑

'''
1. 初始url地址，发送post请求，分析url地址规律
2. 对url地址的响应保存，进行decode 处理
3. elements语义提取，利用xpath, lxml等快速对信息定位，然后保存获取到的信息
'''


import requests
import json
from lxml import etree
from phrasing_url import phrasing_url
from extract_data import extract_data

initial_url = "http://jobs.zhaopin.com/sj894/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.17 Safari/537.36",
    "Referer": "http://jobs.zhaopin.com/sj894/"
}

html = phrasing_url(initial_url, headers)
dic = extract_data(html)


i = 1
while i < 87:
    i = i+1
    url = initial_url+"p"+str(i)+"/"
    html = phrasing_url(url, headers)
    dic.extend(extract_data(html))


with open('zhilianzhaopin.txt', 'w', encoding='utf-8') as f:
    for i in dic:
        f.write(json.dump(dic[i],ensure_ascii=False,indent=2))
        f.write("\n")

