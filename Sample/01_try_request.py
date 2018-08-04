import requests

from PIL import Image
from io import BytesIO

url = "http://www.baidu.com"
response = requests.get(url)
r = requests.get('https://api.github.com/events')
#print(response)

#print(response.text)

jpg_url = 'http://img2.niutuku.com/1312/0804/0804-niutuku.com-27840.jpg'

#content = requests.get(jpg_url).content

#with open('demo.jpg', 'wb') as fp:
#    fp.write(content)

#i = Image.open(BytesIO(r.content))

print(r.raise_for_status())
print(r.status_code)
print(r.headers)

#print(r.json())
