# This function will receive a HTML element and return the an dic that contain the post, company, salary, location, release_data
#from phrasing_url import phrasing_url

def extract_data(html):
    post = html.xpath("//span[@class='post']/a//text()")
    company = html.xpath("//span[@class='company_name']/a//text()")
    salary = html.xpath("//span[@class='salary']//text()")
    address = html.xpath("//span[@class='address']/a//text()")
    release_time = html.xpath("//span[@class='release_time']//text()")
    dic = [{}]
    for i in [0,len(post)-1]:
        job = {
            "post" : post[i],
            "company" : company[i],
            "salary" : salary[i],
            #"address" : address[i],
            "release_time" : release_time[i],
        }
        dic.append(job)
    return dic

