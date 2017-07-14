# -*-coding:utf-8 -*-

import requests
from requests.adapters import HTTPAdapter
import cookielib
import re
import time
import os.path
from PIL import Image


user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5)'
headers = {'User-Agent': user_agent}

session = requests.session()


def get_xsrf():
    index_url = "http://www.zhihu.com"
    index_page = session.get(index_url, headers=headers)
    html = index_page.text
    pattern = r'name="_xsrf" value="(.*?)"'
    _xsrf = re.findall(pattern, html)
    return _xsrf[0]



def getImageUrl():
    url = "https://www.zhihu.com/node/QuestionAnswerListV2"
    method = 'next'
    size = 10
    allImageUrl = []

    #循环直至爬完整个问题的回答
    while(True):
        print '===========offset: ', size
        postdata = {
            'method': 'next',
            'params': '{"url_token":' + str(28205363) + ',"pagesize": "10",' +\
                      '"offset":' + str(size) + "}",
            '_xsrf':get_xsrf(),

        }
        size += 10
        page = session.post(url, headers=headers, data=postdata)
        ret = eval(page.text)
        listMsg = ret['msg']

        if not listMsg:
            print "图片URL获取完毕, 页数: ", (size-10)/10
            return allImageUrl
        pattern = re.compile('data-actualsrc="(.*?)">', re.S)
        for pageUrl in listMsg:
            items = re.findall(pattern, pageUrl)
            for item in items:
                imageUrl = item.replace("\\", "")
                allImageUrl.append(imageUrl)


def saveImagesFromUrl(filePath):
    imagesUrl = getImageUrl()
    print "图片数: ", len(imagesUrl)
    if not imagesUrl:
        print 'imagesUrl is empty'
        return
    nameNumber = 0;
    for image in imagesUrl:
        suffixNum = image.rfind('.')
        suffix = image[suffixNum:]
        fileName = filePath + os.sep + str(nameNumber) + suffix
        nameNumber += 1
        try:
            session.mount(image, HTTPAdapter(max_retries=3))
            response = session.get(image, timeout=20)
            contents = response.content
            with open(fileName, "wb") as pic:
                pic.write(contents)

        except IOError:
            print 'Io error'
        except requests.exceptions.ConnectionError:
            print '连接超时,URL: ', image
    print '图片下载完毕'


saveImagesFromUrl('E:/newpic')