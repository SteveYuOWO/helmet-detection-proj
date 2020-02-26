from selenium import webdriver
from queue import Queue
from urllib import request
import os, gevent
from lxml import etree
import time

cnt = 1


def get_img(html):
    global cnt
    html = html.get()
    html = etree.HTML(html)
    img_url = html.xpath('//div[@id="imgid"]/div[last()]//li/@data-objurl')
    path = './baidupic/'

    if not os.path.exists(path):
        os.makedirs(path)

    for url in img_url:
        try:
            fname = time.strftime("%Y-%m-%d %H:%M:%S ") + str(time.time())[-2:]
            if url[-3:] == 'jpg':
                request.urlretrieve(url, os.path.join(path, fname + '.jpg'))
                print('下载成功' + fname + '.jpg, 已下载' + str(cnt) + '张图片')
                cnt += 1
            elif url[-3:] == 'png':
                request.urlretrieve(url, os.path.join(path, fname + '.png'))
                print('下载成功' + fname + '.png, 已下载' + str(cnt) + '张图片')
                cnt += 1
            else:
                print('格式不支持')
        except:
            print('图片不存在')


def get_page():
    # 创建数据队列
    q = Queue()
    # 百度图片搜索地址
    base_url = 'https://image.baidu.com/'
    # 返回浏览器对象
    browser = webdriver.Chrome('./chromedriver')
    # 模拟访问
    browser.get(base_url)
    # 输入搜索关键字
    browser.find_element_by_id('kw').send_keys('工地')
    # 按键
    browser.find_element_by_class_name('s_search').click()
    # 爬取50个baidu网页进队列
    for i in range(50):
        print("正在爬取第%d张网页" % i)
        browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        q.put(browser.page_source)

    g_list = []
    # 30 个协程一起处理
    for i in range(30):
        g = gevent.spawn(get_img, q)
        g_list.append(g)
    gevent.joinall(g_list)


if __name__ == '__main__':
    get_page()