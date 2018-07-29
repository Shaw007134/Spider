# coding = utf-8

import requests
url = "http://fanyi.baidu.com/basetrans"

query_string = {
    "query": "你好",
    "from": "zh",
    "to": "en"
}

headers = {"User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",
           "Referer":"http://fanyi.baidu.com/",
           "Content-Type": "application/x-www-form-urlencoded"
}

#r = requests.get("http://fanyi.baidu.com")
#print(r.content.decode())
#print(r.content.decode("gbk"))

response = requests.post(url,data=query_string,headers=headers)

print(response.content.decode())
