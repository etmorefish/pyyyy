import re
str1 = '你好$$$我正在学 Python@#@现在需要&*&*修改字符串'
# str2 = str1.replace('$$$',' ').replace('@#@',' ').replace('&*&*',' ')
str2 = re.sub('[$@#&*]+',' ',str1)
print(str2)