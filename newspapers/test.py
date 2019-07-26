from scrapy.cmdline import execute

import time

if __name__ == '__main__':
    stime = time.time()
    execute('scrapy crawl 滨海时报2'.split(' '))
    etime = time.time()
    print('run time {}'.format(etime - stime))
