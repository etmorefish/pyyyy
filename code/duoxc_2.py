#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Date    : 2019-01-15 21:35:38
# @Author  : lilei (849078367@qq.com)
# @Link    : http://www.xxml.xyz
# @Version : $Id$


import threading
import requests
import time
import queue as Queue

link_list = []
with open('alexa200.txt', 'r') as file:
    file_list = file.readlines()
    for eachone in file_list:
        # link = eachone.split('\t')[1]
        link = eachone.replace('\n','')
        link_list.append(link)
        
start = time.time()
class myThread (threading.Thread):
    def __init__(self, name, q):
        threading.Thread.__init__(self)
        self.name = name
        self.q = q
    def run(self):
        print ("Starting " + self.name)
        while True:
            try:
                crawler(self.name, self.q)
            except:
                break
        print ("Exiting " + self.name)
        
def crawler(threadName, q):
    url = q.get(timeout=2)
    try:
        r = requests.get(url, timeout=20)
        print (q.qsize(), threadName, r.status_code, url)
    except Exception as e: 
        print (q.qsize(), threadName, url, 'Error: ', e)
        
threadList = ["Thread-1", "Thread-2", "Thread-3","Thread-4", "Thread-5","Thread-6","Thread-7","Thread-8","Thread-9","Thread-10"]
workQueue = Queue.Queue(200)
threads = []

# 创建新线程
for tName in threadList:
    thread = myThread(tName, workQueue)
    thread.start()
    threads.append(thread)
    
# 填充队列
for url in link_list:
    workQueue.put(url)

# 等待所有线程完成
for t in threads:
    t.join()

end = time.time()
print ('Queue多线程爬虫的总时间为：', end-start)
print ("Exiting Main Thread")