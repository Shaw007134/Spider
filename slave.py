#slave.py

current_url = request_from_master()
to_send = []

for next_url in extract_urls(current_url):
    to_send.append(next_url)

store(current_url);
sent_to_master(to_send)

#master.py
distributed_queue = DistributedQueue()
bf = BloomFilter()

initial_pages = "www.renmingribao.com"

while(True):
    if request == 'GET':
        if distributed_queue.size() > 0:
            send(distributed_queue.get())
        else:
            break
    elif request == 'POST'：
        bf.put(request.url)
        
