#-*- coding:utf-8 -*-

# import urllib
# import urllib2
# import re

# page = 1
# url = "http://www.qiushibaike.com/hot/page/" + str(page)
# user_agent = "Mozilla/4.0(compatible; MSIE 5.5; Windows NT)"
# headers = {'User-Agent': user_agent}
# try:
#     request = urllib2.Request(url, headers = headers)
#     response = urllib2.urlopen(request)
#     content = response.read().decode('utf8')
#     pattern = re.compile('<div class="author clearfix">.*?href.*?<img src.*?title=.*?<h2>(.*?)</h2>.*?<div class="content">(.*?)</div>.*?<i class="number">(.*?)</i>',re.S)
#     items = re.findall(pattern,content)
#     for item in items:
#         for entry in item:
#             print entry.encode('utf-8')
# except urllib2.URLError, e:
#     if hasattr(e, "code"):
#         print e.code
#     if hasattr(e, "reason"):
#         print e.reason
#每一个段子都是<div class=”article block untagged mb15″ id=”…”>…</div>包裹的内容。
#获取发布人，发布日期，段子内容，以及点赞的个数
#段子有些是带图片的，想在控制台显示图片是不现实的，所以直接把带有图片的段子给它剔除掉，只保存仅含文本的段子

#用到的方法是 re.findall 是找寻所有匹配的内容


# 1）.*? 是一个固定的搭配，.和*代表可以匹配任意无限多个字符，加上？表示使用非贪婪模式进行匹配，也就是我们会尽可能短地做匹配，以后我们还会大量用到 .*? 的搭配。

# 2）(.*?)代表一个分组，在这个正则表达式中我们匹配了五个分组，在后面的遍历item中，item[0]就代表第一个(.*?)所指代的内容，item[1]就代表第二个(.*?)所指代的内容，以此类推。

# 3）re.S 标志代表在匹配时为点任意匹配模式，点 . 也可以代表换行符。

#优化和封装

__author__ = 'SN'

import urllib
import urllib2
import re
import thread
import time

#糗事百科爬虫类
class QSBK:
    def __init__(self):
        self.pageIndex = 1
        self.user_agent = "Mozilla/4.0(compatible; MSIE 5.5; Windows NT)"
        self.headers = {'User-Agent': self.user_agent}
        #存放段子的变量
        self.stories = []
        #程序是否继续运行
        self.enable = False

    def getPage(self, pageIndex):
        '''
            传入页码 获取页面代码
        '''
        try:
            url = "http://www.qiushibaike.com/hot/page/" + str(pageIndex)
            request = urllib2.Request(url, headers = self.headers)
            response = urllib2.urlopen(request)
            pageCode = response.read().decode('utf-8')
            return pageCode
        except urllib2.URLError, e:
            if hasattr(e, "reason"):
                print '连接糗事百科失败！原因：', e.reason
                return None

    def getPageItems(self, pageIndex):
        '''
            传入页码 返回不带图片的段子
        '''
        pageCode = self.getPage(pageIndex)
        if not pageCode:
            print '页面加载失败......'
            return None
        pattern = re.compile('<div class="author clearfix">.*?href.*?<img src.*?title=.*?<h2>(.*?)</h2>.*?<div class="content">(.*?)</div>.*?<i class="number">(.*?)</i>',re.S)
        items = re.findall(pattern, pageCode)
        pageStories = []
        for item in items:
            replaceBR = re.compile('<br/>')
            text = re.sub(replaceBR, '\n', item[1])
            pageStories.append([item[0].strip(), text.strip(), item[2].strip()])
        return pageStories

    def loadPage(self):
        '''
            获取页面内容加到列表中
        '''
        if self.enable:
            if len(self.stories) < 2:
                # 获取新一页
                pageStories = self.getPageItems(self.pageIndex)
                if pageStories:
                    self.stories.append(pageStories)
                    self.pageIndex += 1

    def getOneStory(self, pageStories, page):
        '''
            每次敲回车 显示一个段子
        '''
        for story in pageStories:
            input = raw_input()
            self.loadPage()
            if input == "Q":
                self.enable = False
                return
            print u"第%d页\t发布人:%s\t内容:%s\t点赞数:%s\t"%(page, story[0], story[1], story[2])

    def start(self):
        print "正在读取糗事百科，按回车查看新段子，按Q退出"
        self.enable = True
        self.loadPage()
        nowPage = 0
        while self.enable:
            if len(self.stories) > 0:
                pageStories = self.stories[0]
                nowPage += 1
                del self.stories[0]
                self.getOneStory(pageStories, nowPage)

spider = QSBK()
spider.start()