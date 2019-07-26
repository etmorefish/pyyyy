from .base import data

file_name = 'bjrb.py'

# 基本信息
data["spider_class"] = "Bjrb"
data["spider_name"] = "北京日报"
# 时间参数留空
data["base_url"] = "http://bjrb.bjd.com.cn/html/{}/node_1.htm"
data["date_format"] = "%Y-%m/%d"            # 时间格式化
data["paper_hrefs_xpath"] = '//li[@class="3"]/a/@href'

# 版面
data["banner_xpath"] = '//a[@class="fm fl"]/text()[2]'
# 版面图片
data["image_xpath"] = '//img[@id="Bantu"]/@src'
data["pdf_xpath"] = '//div[@class="downPDF"]/a/@href'              # pdf链接
data["article_xpath"] = '//li[@class="area_select"]/h2/a/@href'         # 文章链接
# data["periodical_xpath"] = ''      # 期号

# 文章
data["title_xpath"] = '//div[@class="article"]/h1/text()'                 # 标题
data["leadtitle_xpath"] = '//div[@class="article"]/h2[@class="leading_title"]/text()'
# data["subtitle_xpath"] = ''                                     # 副标题
data["content_xpath"] = '//div[@class="text"]//p/text()'          # 内容
data["image_links_xpath"] = '//div[@class="text"]//img/@src'      # 图片link
# data["images_desc_xpath"] = ''
# data["author_xpath"] = ''           # 作者
# data["reporter_xpath"] = ''         #
# data["keywords_xpath"] = ''         # 关键字【多半没有】
# data["source_xpath"] = ''           # 来源【多半没有】
# data["is_original_xpath"] = ''      # 是否原创【多半没有】
