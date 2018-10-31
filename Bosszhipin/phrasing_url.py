import requests
from lxml import etree

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.17 Safari/537.36",
    "Referer": "https://www.zhipin.com/job_detail/?query=%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90&scity=101280600&source=8",
}

def phrasing_url(initial_url):
    response = requests.get(initial_url,headers=headers)
    html_str = response.content.decode()
    html = etree.HTML(html_str)
    return html

#def _phrasing_url():
if __name__ == '__main__':
    initial_url = "https://www.zhipin.com/c100010000/?query=%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E5%B8%88&page=2&ka=page-2"

    html = phrasing_url(initial_url)
    post = html.xpath("//div[@class='job-title']//text()")
    print(post)