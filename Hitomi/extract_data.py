from phrasing_url import phrasing_url

def extract_data(html):
  html = phrasing_url(html)
  img_url_unitia = html.xpath("//div[@class='img-url']//text()")

  for i in range(len(img_url_unitia)):
    img_url_unitia[i] = "https://ba" + img_url_unitia[i].split('//g')[1]
  return img_url_unitia