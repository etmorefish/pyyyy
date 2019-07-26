from .base import data

file_name = 'bjbusiness.py'

# 基本信息
data["spider_class"] = "Bjb"
data["spider_name"] = "北京商报"
# 时间参数留空
data["base_url"] = "http://epaper.bjbusiness.com.cn/site1/bjsb/html/{}/node_205.htm"
data["date_format"] = "%Y-%m/%d"            # 时间格式化
data["paper_hrefs_xpath"] = '//a[@id="pageLink"]/@href'

# 版面
data["banner_xpath"] = '//td[@class="px12" and @align="left"]//text()'
# 版面图片
data["image_xpath"] = '//img[@usemap="#PagePicMap"]/@src'
data["pdf_xpath"] = '//a[contains(@href, "pdf.pdf")]/@href'              # pdf链接
data["article_xpath"] = '//a[contains(@href, "content")]/@href'         # 文章链接
# data["periodical_xpath"] = ''      # 期号

# 文章
data["title_xpath"] = '//tr[@valign="top"]/td/strong/text()'                 # 标题
# data["leadtitle_xpath"] = '//div[@class="article"]/h2[@class="leading_title"]/text()'
# data["subtitle_xpath"] = ''                                     # 副标题
data["content_xpath"] = '//div[@id="ozoom"]//p/text()'          # 内容
data["image_links_xpath"] = '//div[@id="ozoom"]//img/@src'      # 图片link
# data["images_desc_xpath"] = ''
# data["author_xpath"] = ''           # 作者
# data["reporter_xpath"] = ''         #
# data["keywords_xpath"] = ''         # 关键字【多半没有】
# data["source_xpath"] = ''           # 来源【多半没有】
# data["is_original_xpath"] = ''      # 是否原创【多半没有】
