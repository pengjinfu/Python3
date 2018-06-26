#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Authour:Dreamer
# Tmie:2018.6.17

import urllib.request
import urllib.parse
import json
import time
import gzip
import random
import hashlib
from tkinter import Tk, Button, Entry, Label, Text, END


class YouDaoFanyi(object):
    def crawl(self, word):
        url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
        data = {}
        head = {}
        ctime = int(time.time() * 1000)
        r = str(ctime + random.randint(1, 10))
        s = 'fanyideskweb'
        d = 'aNPG!!u6sesA>hBAW1@(-'
        data['i'] = word
        data['from'] = 'AUTO'
        data['to'] = 'AUTO'
        data['smartresult'] = 'dict'
        data['client'] = 'fanyideskweb'
        data['salt'] = r
        data['sign'] = hashlib.md5((s + word + r + d).encode('utf-8')).hexdigest()
        data['doctype'] = 'json'
        data['version'] = '2.1'
        data['keyfrom'] = 'fanyi.web'
        data['action'] = 'FY_BY_CLICKBUTTION'
        data['typoResult'] = 'false'
        head['Accept'] = 'application/json, text/javascript, */*; q=0.01'
        head['Accept-Encoding'] = 'gzip, deflate'
        head['Accept-Language'] = 'zh-CN,zh;q=0.9'
        head['Connection'] = 'Keep-Alive'
        head['Content-Type'] = 'application/x-www-form-urlencoded; charset=UTF-8'
        head[
            'Cookie'] = 'OUTFOX_SEARCH_USER_ID=-1645744815@10.169.0.84; JSESSIONID=aaa9_E-sQ3CQWaPTofjew; OUTFOX_SEARCH_USER_ID_NCOO=2007801178.0378454; fanyi-ad-id=39535; fanyi-ad-closed=1; ___rl__test__cookies=' + str(
            ctime)
        head['Host'] = 'fanyi.youdao.com'
        head['Origin'] = 'http://fanyi.youdao.com'
        head['Referer'] = 'http://fanyi.youdao.com/'
        head[
            'User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
        head['X-Requested-With'] = 'XMLHttpRequest'
        data = urllib.parse.urlencode(data).encode('utf-8')
        req = urllib.request.Request(url, data, head)
        response = urllib.request.urlopen(req)
        with gzip.open(response, 'rb') as f:
            html = f.read()
        target = json.loads(html)
        result = target['translateResult'][0][0]['tgt']
        return result


class Application(object):
    def __init__(self):
        self.window = Tk()
        self.fanyi = YouDaoFanyi()

        self.window.title(u'Python简易翻译器')
        # 设置窗口大小和位置
        self.window.geometry('800x400+500+300')
        self.window.minsize(800, 400)
        self.window.maxsize(800, 400)
        # 创建一个文本框
        # self.entry = Entry(self.window)
        # self.entry.place(x=10,y=10,width=200,height=25)
        # self.entry.bind("<Key-Return>",self.submit1)
        self.result_text1 = Text(self.window, background='#ffffff')
        self.result_text1.place(x=10, y=5, width=780, height=195)
        self.result_text1.bind("<Key-Return>", self.submit1)

        # 创建一个按钮
        # 为按钮添加事件
        self.submit_btn = Button(self.window, text=u'自动翻译', command=self.submit)
        self.submit_btn.place(x=170, y=140, width=120, height=50)
        self.submit_btn2 = Button(self.window, text=u'清空', command=self.clean)
        self.submit_btn2.place(x=300, y=140, width=70, height=50)

        # 翻译结果标题
        self.title_label = Label(self.window, text=u'翻译结果:')
        self.title_label.place(x=10, y=165)
        # 翻译结果

        self.result_text = Text(self.window, background='#ffffff')
        self.result_text.place(x=10, y=190, width=780, height=195)
        # 回车翻译

    def submit1(self, event):
        # 从输入框获取用户输入的值
        content = self.result_text1.get(0.0, END).strip().replace("\n", " ")
        # 把这个值传送给服务器进行翻译

        result = self.fanyi.crawl(content)
        # 将结果显示在窗口中的文本框中

        self.result_text.delete(0.0, END)
        self.result_text.insert(END, result)

        # print(content)

    def submit(self):
        # 从输入框获取用户输入的值
        content = self.result_text1.get(0.0, END).strip().replace("\n", " ")
        # 把这个值传送给服务器进行翻译

        result = self.fanyi.crawl(content)
        # 将结果显示在窗口中的文本框中

        self.result_text.delete(0.0, END)
        self.result_text.insert(END, result)
        print(content)

    # 清空文本域中的内容
    def clean(self):
        self.result_text1.delete(0.0, END)
        self.result_text.delete(0.0, END)

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    app = Application()
    app.run()
