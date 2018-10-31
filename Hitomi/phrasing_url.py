import requests
from lxml import etree
from retrying import retry
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.17 Safari/537.36",
    "Referer": "",
}
@retry(stop_max_attempt_number=3)
def phrasing_url(initial_url): 
    headers['Referer'] = initial_url
    url = initial_url
    print("Phrasing url: {}".format(url))
    try:
        response = requests.get(url,headers=headers,timeout=3)
        html_str = response.content.decode()
        html = etree.HTML(html_str)
    except:
        html = None
    return html  