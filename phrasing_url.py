### This function will take url and return html elements
import requests
from lxml import etree

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.17 Safari/537.36",
    "Referer": "http://jobs.zhaopin.com/sj894/",
}

def phrasing_url(initial_url):
    response = requests.get(initial_url,headers=headers)
    html_str = response.content.decode()
    html = etree.HTML(html_str)
    return html

#def _phrasing_url():
if __name__ == '__main__':
    initial_url = "http://jobs.zhaopin.com/sj894/"

    html = phrasing_url(initial_url)
    print(html)