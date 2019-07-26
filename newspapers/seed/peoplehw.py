from .base import data

file_name = 'peoplehw.py'

# 基本信息
data["spider_class"] = "PeopleHw"
data["spider_name"] = "人民日报-海外"
# 时间参数留空
data["base_url"] = "http://paper.people.com.cn/rmrbhwb/html/{}/node_865.htm"
data["date_format"] = "%Y-%m/%d"            # 时间格式化
data["paper_hrefs_xpath"] = '//a[@id="pageLink"]/@href'

# 版面
data["banner_xpath"] = '//div[@class="l_t"]/text()'
# 版面图片
data["image_xpath"] = '//div[@class="ban"]/div/img/@src'
data["pdf_xpath"] = '//div[@class="ban_t"]/div/ul/li/a/@href'              # pdf链接
data["article_xpath"] = '//div[@id="titleList"]/ul/li/a/@href'         # 文章链接
# data["periodical_xpath"] = ''      # 期号

# 文章
data["title_xpath"] = '//div[@class="text_c"]/h1/text()'                 # 标题
# data["leadtitle_xpath"] = ''
# data["subtitle_xpath"] = ''                                     # 副标题
data["content_xpath"] = '//div[@id="ozoom"]//p/text()'          # 内容
data["image_links_xpath"] = '//table[@class="pci_c"]//img/@src'      # 图片link
# data["images_desc_xpath"] = ''
# data["author_xpath"] = ''           # 作者
# data["reporter_xpath"] = ''         #
# data["keywords_xpath"] = ''         # 关键字【多半没有】
# data["source_xpath"] = ''           # 来源【多半没有】
# data["is_original_xpath"] = ''      # 是否原创【多半没有】
