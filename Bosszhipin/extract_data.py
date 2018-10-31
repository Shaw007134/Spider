from phrasing_url import phrasing_url

def extract_data(html):
    post = html.xpath("//div[@class='job-title']//text()")
    company = html.xpath("//div[@class='company-text']//a//text()")
    print(company)
    company_dec = html.xpath("//div[@class='company-text']//p//text()")
    salary = html.xpath("//span[@class='red']//text()")
    detail_url = html.xpath("//div[@class='info-primary']/h3/a/@href")
    dic =[]
    for i in range(0,len(post)):
      # print("Company: " + company[i])
      # print("https://www.zhipin.com" + detail_url[i])
      desc = phrasing_url("https://www.zhipin.com" + detail_url[i])
      info = desc.xpath("//div[@class='info-primary']/div[@class='job-author']//following-sibling::p/text()")
      release_time = str(desc.xpath("//span[@class='time']//text()")).split('发布于')[1].split(' ')[0]
    #   post_ul = str(desc.xpath("//div[@class='job-sec']/div[@class='text']//text()")).split('                                    ')[1]
      post_ul = str(desc.xpath("//div[@class='job-sec']/div[@class='text']//text()"))
      job_tag = str(desc.xpath("//div[@class='job-tags']//span//text()"))
      company_info = str(desc.xpath("//div[@class='job-sec company-info']/div[@class='text']//text()"))
      job = {
          "post" : post[i],
          "company" : company[i],
          "company_dec": company_dec[i],
          "salary" : salary[i],
          "release_time" : release_time,
          "address" : info[0].split('：')[1],
          "experience": info[1].split('：')[1],
          "graduation": info[2].split('：')[1],
          # 'requirment':requirement,
          # 'profile' : profile,
          "post_ul" : post_ul,
          "job_tag": job_tag,
          "company_info": company_info,
      }
      print(company[i])
      dic.append(job)
    return dic


#def _phrasing_url():
if __name__ == '__main__':
    initial_url = "https://www.zhipin.com/c101280600/?query=%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90&page=2&ka=page-2"
    html = phrasing_url(initial_url)
    dic = extract_data(html)
    for job in dic:
        for key, value in job.items():
            print(key + ": " + value)