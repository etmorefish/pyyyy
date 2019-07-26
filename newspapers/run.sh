#!/bin/bash
source /home/crawl/www/bin/activate

cd /home/crawl/xwcj/newspapers

LOG_FILE='/home/crawl/xwcj/log/runtime.log'

starttime=`date +'%Y-%m-%d %H:%M:%S'`

scrapy crawlall -a total=$1 -a page=$2

endtime=`date +'%Y-%m-%d %H:%M:%S'`
start_seconds=$(date --date="$starttime" +%s);
end_seconds=$(date --date="$endtime" +%s);

echo "newspaper total=$1 page=$2 starttime: ${starttime} endtime: ${endtime} 运行时间："$((end_seconds-start_seconds))"s" >> "${LOG_FILE}"
#echo "newspaper starttime: ${starttime} endtime: ${endtime} 运行时间："$((end_seconds-start_seconds))"s" >> "${LOG_FILE}"
