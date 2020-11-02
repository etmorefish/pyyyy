from PIL import Image

img = Image.open('./yiwu.png')
name = 'yiwu.png'.split('.')
img.save('./'+name[0]+'.jpg')