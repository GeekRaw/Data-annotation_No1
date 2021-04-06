# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 09:07:27 2020

@author: 虫二
"""


import requests
import time
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import json

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
            "Cookie": "device_id=bd43492b7a85e5d94101bda778256023; acw_tc=2760820116154239892348120e59513794f6b3b1c60e440e76334fdd0f9bac; Hm_lvt_1db88642e346389874251b5a1eded6e3=1614869350,1615026899,1615026916,1615423990; s=ea12gxzx1g; xq_a_token=1f2f0960b6b7cfbc2610260a7e6874a67c334e88; xqat=1f2f0960b6b7cfbc2610260a7e6874a67c334e88; xq_r_token=4b3f2b3595277469bbb479ffc44c13a556b82c1a; xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOjU3OTE0MjkxNTIsImlzcyI6InVjIiwiZXhwIjoxNjE4MDE2MDYzLCJjdG0iOjE2MTU0MjQwNjM3NDUsImNpZCI6ImQ5ZDBuNEFadXAifQ.EUtf3vCgr_hP-XVpLIZOWabgztEiiHK3TE_u3oJAkm4r1Nusa51hQP2K6vQES5RUJNHy_bZrsagg1inn1EcLrU-2V5ke388HpsDiJnv_wB_9wx74wWMXhveuOMuC8Hv6NBAdNfrfEP4AxA5RnRqJEzbmq9S4AzzsJpBi3_UugtCsZpGMTC6r7628hkgff1rtQZ4OBG2aQH2kEivkskGBz0crcrnYEsiSVzwun6v6Ltit9qY81UtYRJBNsAZEvh1-993x8i06sYDfseQNcH56rLEpnazIK0Gg0vgqmeBBLrSZZHbdD1-5nJuBOgdfhgIwtnX8BceQX3Kl5Qq8ZOhYUA; xq_is_login=1; u=5791429152; snbim_minify=true; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1615424131"
        }
 
    def run(self):
        symbol = 'SH601318'     # 输入股票代码
        for i in range(100):
            detail_url = "https://xueqiu.com/statuses/search.json?count=10&comment=0&symbol={}&hl=0&source=all&sort=&page={}&q=&type=11".format(
                symbol, i + 1)
            print(detail_url)
            try:
                content_list, count = self.parse_comment_url(detail_url)
                time.sleep(5)   # 等待5秒，时间越长越不容易被网站检测到
            except Exception as e:  # 捕获错误信息
                print("Error:", e)
                time.sleep(5)
                content_list = self.parse_comment_url(detail_url)   # 失败后再次尝试获取
                time.sleep(5)
            self.save_file(content_list)
 
    def parse_comment_url(self, url):
        r = requests.get(url, headers=self.headers,proxies=proxies, verify=False)   # 发送请求
        res_list = r.json()['list'] # 存储返回的json中list
#        print(res_list) # test
        count = r.json()['count']
        content_list = []
        for res in res_list:
            item = {}
            item['user_name'] = res['user']['screen_name']
            if 'description' in res['user']:    # 先检查是否有description元素
                item['user_description'] = res['user']['description']   # 用户描述，个性签名之类的
            item['comment_title'] = res['title']
            item['comment_text'] = res['text']
            content_list.append(item)
        return content_list, count
 
    def save_file(self, content_list):
        for content in content_list:
            #保存为文件名xueqiu_comment的文件
            with open('xueqiu_comment.json', 'a')as f:
                f.write(str(content).encode("gbk", 'ignore').decode("gbk", "ignore"))
                f.write("\n")
            
# https://www.cnblogs.com/zhangyinhua/p/8037599.html
if __name__ == '__main__':
    xueqiu = Xueqiuspider()
    xueqiu.run()
    #getStockData()