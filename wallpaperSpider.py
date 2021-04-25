from urllib.request import urlretrieve

import requests
import os
from bs4 import BeautifulSoup

"""
    Author:
        faith
"""

# 创建保存目录
save_dir = '王者荣耀壁纸'
if save_dir not in os.listdir('./'):
    os.mkdir(save_dir)

target_url = "https://pic.netbian.com/4kmeinv/index.html"

c = dict(__cfduid='d4b73ec234787152ae681aef0113bea321618457455',Hm_lvt_14b14198b6e26157b7eba06b390ab763='1618457452',zkhanecookieclassrecord='%2C54%2C',Hm_lpvt_14b14198b6e26157b7eba06b390ab763='1618749416',Hm_lvt_526caf4e20c21f06a4e9209712d6a20e='1618583922,1618745706,1618750172',PHPSESSID='2af8ojr6ti1b3jlqs4vicfleh2',zkhanmlusername='qq354664161875',zkhanmluserid='4824094',zkhanmlgroupid='1',zkhanmlrnd='7j9RuoV6LUQLkZslHyqY',zkhanmlauth='1afc4f259e27fb09b6dc585d39b762fd',Hm_lpvt_526caf4e20c21f06a4e9209712d6a20e='1618751363',zkhandownid27244='1')

flag = True
while flag:
    print(target_url)
    # 获取壁纸页面
    r = requests.get(url=target_url, cookies=c)

    print(r.content)
    exit('测试')

    bs = BeautifulSoup(r.content, 'lxml')

    list_con_li = bs.find('div', class_="list")

    pages = bs.find_all('a', class_="prev")

    # cartoon_list = list_con_li.find_all('img')
    cartoon_list = list_con_li.find_all('a')

    chapter_names = []
    chapter_urls = []
    img_info = {}
    for page in pages:
        if page.find('下一页') == -1:
            flag = False
        else:
            target_url = target_url[0:22] + page['href']
            flag = True
    for cartoon in cartoon_list:
        href = cartoon["href"]
        if href.find('desk') == -1:
            continue
        name = cartoon.b.string
        chapter_names.insert(0, name)
        new_href = href.replace('small', '')
        big_img_html = target_url[0:22] + new_href[0:-4] + "-1920x1080.htm"
        a = requests.get(url=big_img_html)
        try:
            result_href = BeautifulSoup(a.content, 'lxml').find('table', id='endimg').find('a')['href']
        except:
            continue
        else:
            chapter_urls.insert(0, result_href)
            img_info[name] = result_href

    # 下载图片
    for title, im_url in img_info.items():
        print(title, im_url)
        if im_url.find('http') == -1:
            continue
        if title.find('2014巴西世界杯32强球衣足球宝贝') != -1:
            title = '2014巴西世界杯32强球衣足球宝贝,大尺度美女桌面壁纸.jpg'
        urlretrieve(im_url, "D:\girls\\" + title + im_url[-4:])
