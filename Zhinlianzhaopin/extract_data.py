# This function will receive a HTML element and return the an dic that contain the post, company, salary, location, release_data

from phrasing_url import phrasing_url
from clearlist import clearlist

def extract_data(html):
    post = html.xpath("//span[@class='post']/a//text()")
    company = html.xpath("//span[@class='company_name']/a//text()")
    salary = html.xpath("//span[@class='salary']//text()")
    address = html.xpath("//span[@class='address']/a//text()")
    release_time = html.xpath("//span[@class='release_time']//text()")
    detail_url = html.xpath("//span[@class='post']/a/@href")
    dic =[]
    for i in range(0,len(post)-1):
        desc = phrasing_url(detail_url[i])
        pos_ul=desc.xpath("(//div[@class='tab-inner-cont'])[1]//text()")
        requirement = desc.xpath("//ul[@class='terminal-ul clearfix']//text()")
        profile = desc.xpath("//ul[@class='terminal-ul clearfix terminal-company mt20']//text()")
        pos_ul = clearlist(pos_ul)
        requirement = clearlist(requirement)
        profile = clearlist(profile)
        job = {
            "post" : post[i],
            "company" : company[i],
            "salary" : salary[i],
            "release_time" : release_time[i],
            "address" : address[i],
            'requirment':requirement,
            'profile' : profile,
            "post_ul" : pos_ul,
        }
        dic.append(job)
    return dic

