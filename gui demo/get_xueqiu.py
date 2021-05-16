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
            #"Cookie": "acw_tc=2760820016194498366047112eee5f1359208a4a511b9846b79edd0fe2659a; Hm_lvt_1db88642e346389874251b5a1eded6e3=1619449844; device_id=24700f9f1986800ab4fcc880530dd0ed; s=cf12e4n8uv; xq_a_token=d7215dcf4ba0097adbc061423091fcd5d2b63e56; xqat=d7215dcf4ba0097adbc061423091fcd5d2b63e56; xq_r_token=5888fab6549ab59eab2f75c633e66c8d4d5e69f3; xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOjEzMTM3ODI0NTUsImlzcyI6InVjIiwiZXhwIjoxNjIxMjQ0NDIzLCJjdG0iOjE2MTk0NDk5MjYzMjEsImNpZCI6ImQ5ZDBuNEFadXAifQ.eD6BRBJb2F5GvUdaVz4RRaRU1JFqv-BWBAw_g6zD1VVsRiqykJ-DMpAeosf1TMoyFOSLrAADQ9ta_EhiGgovZsJZnXI8UZYUSEWJNglYt1rf8YuIlgVQEcoDSx3jmLtehR6axH0P1ySS7MGB9_7FbQoy8yl61BfyoO7NxaYEIf_KyFq6tmHSoE5OLMJiNjrptrAIcoTVk81M9AQ3HWoVqegCvlFY1uSwW5ei833iGmL7DW_hoL6NEcglxoC83YFKjsO4Nk4B7HrMKjVGVcL9HRod43U73Xbicyw3vGFDD6V20Gqp4XsSWl8P-ph715VGhZ6QhB09C7Ink_t9iCQcvg; xq_is_login=1; u=1313782455; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1619450018"
            
            "Cookie":"acw_tc=2760820016194916035896329eee3bad4ea9305332aaf4ed39217b069c05b3; device_id=24700f9f1986800ab4fcc880530dd0ed; Hm_lvt_1db88642e346389874251b5a1eded6e3=1619491605; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1619491605; s=di15tltj2o; xq_a_token=d7215dcf4ba0097adbc061423091fcd5d2b63e56; xqat=d7215dcf4ba0097adbc061423091fcd5d2b63e56; xq_r_token=5888fab6549ab59eab2f75c633e66c8d4d5e69f3; xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOjEzMTM3ODI0NTUsImlzcyI6InVjIiwiZXhwIjoxNjIxMjQ0NDIzLCJjdG0iOjE2MTk0OTE3MjEzMTAsImNpZCI6ImQ5ZDBuNEFadXAifQ.VgarpJA7hOIDh039MzvM2jATnTUqmgXcBS4j3XgOLVrsOOpDL1PHsoZMfMmP5KrJuDdJVexAWYgvUCehs0PveVkhHwKF6E8HiM_QTfTi6JiTf4dEC01GegUGrIPntgkSrZfsshh6ejGjg9AzeufG0g5Ozfu5OGHZbNkwMxciFNhapK0zuG-X0V4Q1_yp32Ys-TeXCaF9VrPJTgNPNYJEERqGwS6C-eFDYdYg6FXMQJ079yEMKV8MbOI0RG11INBNz8OeUnk7B3CfwRZajdOEhoHd43aC_jhWLsNAXdrsfkrRSIJyOzQsyKcPu8mTvhV7_h_AR2QHrjpXlcQCPFPUeg; xq_is_login=1; u=1313782455"
        }
    
    #传入一个股票代码,传入一个进度条，显示进度,单独使用一个线程运行，在循环中设置一个标志位，点击停止时退出
    #还要传入进度条所在的窗口
    def run(self,stock_num,dwin,download_progress,flag):
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
                    time.sleep(3)   # 等待3秒，时间越长越不容易被网站检测到
                   
                    #更新进度条
                    download_progress['value']+=10
                    dwin.update()
                except Exception as e:  # 捕获错误信息
                    print("Error:", e)
                    time.sleep(5)
                    content_list = self.parse_comment_url(detail_url)   # 失败后再次尝试获取
                    time.sleep(5)
                    download_progress['value']+=10
                    dwin.update()
                self.save_file(content_list)
            else:
                break
 
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