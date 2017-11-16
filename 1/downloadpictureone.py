import requests
from bs4 import BeautifulSoup
import os
#获取html
f = requests.get('https://www.deviantart.com/?offset=0')
#用BS解析html
soup = BeautifulSoup(f.text, 'lxml')
s_imgs = soup.find_all('img')
#逐个将图片保存到本地
i=1
for s_img in s_imgs:
    img_url = s_img['src']
    img_content = requests.get(img_url).content
    file_name = str(i) + '.png'
    with open(os.getcwd()+'/'+file_name, 'wb') as file:
        file.write(img_content)
    i += 1


'''
粗略下载图片，存在图片格式问题
'''