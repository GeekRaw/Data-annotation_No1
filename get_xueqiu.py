# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 09:07:27 2020
@author: 虫二
"""

import os
import requests
import time
import urllib3
import re

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import json
import tkinter
from tkinter import*
from tkinter import ttk



proxies = {
#	"http" : "http://111.222.141.127:8118" # 代理ip
}

class Xueqiuspider:
    def __init__(self):
        self.start_url = 'https://xueqiu.com/service/v5/stock/screener/quote/list?page={}&size=30&order=desc&order_by=percent&exchange=CN&market=CN&type=sha&'
        self.headers = {
            "Host": "xueqiu.com",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36",
            "Referer": "https://xueqiu.com/hq",
            # 登录后的cookie，雪球网有个反扒机制，登录账号后才能查看页面信息
            # Cookie需要定期更新
          
            #"Cookie":"acw_tc=2760820016232444386198686e11a71631f62447b27556f7b16c8eb8e15067; device_id=24700f9f1986800ab4fcc880530dd0ed; Hm_lvt_1db88642e346389874251b5a1eded6e3=1623244440; s=d617pver10; xq_a_token=393557f1b4b7849e29b5c9a4ff32edc8fc1d8459; xqat=393557f1b4b7849e29b5c9a4ff32edc8fc1d8459; xq_r_token=36399c8ddde5b06aea1dc341e74463d687cac653; xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOjEzMTM3ODI0NTUsImlzcyI6InVjIiwiZXhwIjoxNjI0MzI1MTU0LCJjdG0iOjE2MjMyNDQ0NTM4NjAsImNpZCI6ImQ5ZDBuNEFadXAifQ.Ryq-KOzXoUYK1XwA0JSVkvfPV70anuAyWffe5-LxIA7xtsSkC9A0d0tt8YaiNGFLJV8UgHapczuJO0GFBPf5cc7xVyR9F1nKtoDnN8lgNZjIE_UxRCfijC8xi5OsbvygymGSsA5NY9SxJ6GtoMrFePrvirmT7ODSjWs7yoCqlIYT_Zdza499LdAQevAhNz5gXOxmAQlGOhE5OKpOYlZNBG4Qf3frLtgbnddEMKr491hn_YUU-niS1okYpVGt5G2S4G3TlETNrKX4JCrULn8DbCOZcqyt2xcc7qlxA5hV2UZ_9PuEJ182OzzwnP_q2hZwLFO3nnFb2LwZqzaTojYnZQ; xq_is_login=1; u=1313782455; is_overseas=0; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1623244490"
            "Cookie":"acw_tc=2760820916234916782527808e894730bf579871fb63dd707595fac5801ad7; device_id=24700f9f1986800ab4fcc880530dd0ed; Hm_lvt_1db88642e346389874251b5a1eded6e3=1623491681; s=c71rr4dels; xq_a_token=393557f1b4b7849e29b5c9a4ff32edc8fc1d8459; xqat=393557f1b4b7849e29b5c9a4ff32edc8fc1d8459; xq_r_token=36399c8ddde5b06aea1dc341e74463d687cac653; xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOjEzMTM3ODI0NTUsImlzcyI6InVjIiwiZXhwIjoxNjI0MzI1MTU0LCJjdG0iOjE2MjM0OTE3Mzc5NDIsImNpZCI6ImQ5ZDBuNEFadXAifQ.hQ6uaWM7vFphIagcPvjyZv6BkGhNxpLl1AjHf6Ko9MLDJi3TXKIRz9bXVvBYv-HmrT8RRn0xS4Sug1CAacWrkkM6kBHtzYLh0WA3VWX77H7qozcY9M1SWaHsdfybDhHq6jlY7efhVAI7eybifN3W5O8u_zRWsvU9C57oR9ErD4BmsAiMYMUSGz_EQpi0kjmJSsjNjIk_m1AKZZ0Cr-Vz_Obp-lHaqcsERP-RI8qOgYS7m_2ppukh1HHo16ueYs-PlmOSkjZZ_U1HIIKWd7pGbNK_pDCZgosg-tfjNIL-bSNi3EnZhlIywrY2LWnMAxf3X2ovwdvfOSs00tMT7oy5Pg; xq_is_login=1; u=1313782455; is_overseas=0; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1623491740"
        }
    
    #传入一个股票代码,传入一个进度条，显示进度,单独使用一个线程运行，在循环中设置一个标志位，点击停止时退出
    #还要传入进度条所在的窗口
    def run(self,start_download,stock_num,dwin,download_progress,flag):
        #symbol = 'SH601318'     # 输入股票代码
        symbol=stock_num
        for i in range(10):
            detail_url = "https://xueqiu.com/statuses/search.json?count=10&comment=0&symbol={}&hl=0&source=all&sort=&page={}&q=&type=11".format(
                symbol, i + 1)
            print(detail_url)
            if flag[0]==1:
                try:
                #设置标志位判断是否退出循环
               
                    content_list, count = self.parse_comment_url(detail_url)
                    time.sleep(2)   # 等待2秒，时间越长越不容易被网站检测到
                   
                    #更新进度条
                    download_progress['value']+=10
                    dwin.update()
                except Exception as e:  # 捕获错误信息
                    print("Error:", e)
                    time.sleep(3)
                    content_list = self.parse_comment_url(detail_url)   # 失败后再次尝试获取
                    time.sleep(3)
                    download_progress['value']+=10
                    dwin.update()
                self.save_file(content_list)
            else:
                tkinter.messagebox.showinfo('提示','下载已经停止')
                break
        if flag[0]==1:
            tkinter.messagebox.showinfo('提示','下载完成')
        start_download['state']=NORMAL
 
    def parse_comment_url(self, url):
        r = requests.get(url, headers=self.headers,proxies=proxies, verify=False)   # 发送请求
        res_list = r.json()['list'] # 存储返回的json中list
#        print(res_list) # test
        count = r.json()['count']
        content_list = []
        
        for res in res_list:
            
            item = {}
            #item['user_name'] = res['user']['screen_name']
            #if 'description' in res['user']:    # 先检查是否有description元素
             #   item['user_description'] = res['user']['description']   # 用户描述，个性签名之类的
            #item['comment_title'] = res['title']
            #item['comment_text'] = res['text']
            item['comment_text']=res['text']
            #正则，去掉一些不需要的字符
            item['comment_text']=re.sub(u"<.*?>||\$||//||&nbsp;",'',item['comment_text'])
            #添加标志位
            item['tag'] = '0'
           
            content_list.append(item)
        return content_list, count
 
    def save_file(self, content_list):
        print('保存评论')
        print('content_list长度:',len(content_list))
        for content in content_list:
            #保存为文件名xueqiu_comment的文件
            print(content)
            
            with open('xueqiu_comment.json', 'a')as f:
                f.write(str(content).encode("gbk", 'ignore').decode("gbk", "ignore"))
                f.write("\n")
            
# https://www.cnblogs.com/zhangyinhua/p/8037599.html
if __name__ == '__main__':
    xueqiu = Xueqiuspider()
    xueqiu.run()
    #getStockData()