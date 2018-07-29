import Queue

initial_page = "http://www.renminribao.com"

url_queue = Queue.Queue()
seen = set()

seen.insert(initial_page)
url_queue.put(initial_page)

while(True): #一直进行
    if url_queue.size()>0:
        current_url = url_queue.get() #拿出队列第一个url
        store(current_url)            #把这个url代表的网页存储好
        for next_url in extract_urls(current_url)： #提取这个url里链向的url
            if next_url not in seen:
                seen.put(next_url)
                url_queue.put(next_url)
    else:
        break
                    
