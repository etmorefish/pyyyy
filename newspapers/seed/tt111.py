data = {}
# 基本信息
data["spider_class"] = "XWNET"
data["spider_name"] = "新晚报数字报"
# 时间参数留空
data["base_url"] = "http://xwb.my399.com/html/{}/node_22.htm"  #新晚报数字报
data["date_format"] = "%Y-%m/%d"            # 时间格式化
data["paper_hrefs_xpath"] = '//td[@class="ft12h"]/a[@class="ft12h"]/@href'

# 版面
data["banner_xpath"] = 'string(//table[@class="ft12h"]//td[@class="px12"])'
# 版面图片
data["image_xpath"] = '//td[@height="533"]/img/@src'
data["pdf_xpath"] = '//table[@class="ft12h"]//a[contains(@href,'pdf')]/@href'              # pdf链接
data["article_xpath"] = '//table[@class="ft12h"]//td[@align="left"]//table/tbody//a/@href'          # 文章链接
# data["periodical_xpath"] = ''       # 期号

# 文章
data["title_xpath"] = '//td[@class="bt11"]/text()'            # 标题
# data["leadtitle_xpath"] = ''
# data["subtitle_xpath"] = ''         # 副标题
data["content_xpath"] = '//div[@id="ozoom"]//p/text()'          # 内容
data["image_links_xpath"] = '//td[@class="ft11"]//img/@src'      # 图片link
data["images_desc_xpath"] = 'string(//td[@class="ft11"])'
# data["author_xpath"] = ''           # 作者
# data["reporter_xpath"] = ''
# data["keywords_xpath"] = ''         # 关键字【多半没有】
# data["source_xpath"] = ''           # 来源【多半没有】
# data["is_original_xpath"] = ''      # 是否原创【多半没有】
