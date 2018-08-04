import requests
from retrying import retry

'''
专门请求url地址的方法
'''

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.17 Safari/537.36"}

@retry(stop_max_attempt_number=3) #让被装饰的函数反复执行三次，三次全部报错才报错
def _parse_url(url):
    print("*"*100)
    response = request.get(url,headers=headers,timeout=5)
    return response.content.decode()

def parse_url(url):
    try:
        html_str = _parse_url(url)
    except:
        html_str = None
    return html_str
    

if __name__ == '__main__':
    url = "http://www.baidu.com"
    url1 = "www.baidu.com"
    #print(parse_url(url)[:100])
    print(parse_url(url1))
