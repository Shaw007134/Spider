#主要逻辑

'''
1. 初始url地址，发送post请求，分析url地址规律
2. 对url地址的响应保存，进行decode 处理
3. elements语义提取，利用xpath, lxml等快速对信息定位，然后保存获取到的信息
'''


import json
from phrasing_url import phrasing_url
from extract_data import extract_data

initial_url = "http://jobs.zhaopin.com/sj894/"


html = phrasing_url(initial_url)
dic = extract_data(html)


i = 1

'''
while i < 87:
    i = i+1
    url = initial_url+"p"+str(i)+"/"
    html = phrasing_url(url)
    dic.extend(extract_data(html))
'''



with open('zhilianzhaopin.txt', 'w', encoding='utf-8') as f:
    for i in dic:
        f.write(json.dumps(i,ensure_ascii=False,indent=2))
        f.write("\n")

