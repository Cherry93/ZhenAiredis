# encoding:utf-8
import urllib
import urllib
# import  urllib.request
# import urllib.parse
# url="https://movie.douban.com/j/chart/top_list?type=10&interval_id=100%3A90&action"
# formdata={"limit":"20","start":"0"} #
# data=urllib.parse.urlencode(formdata).encode(encoding='UTF8')
#  #编码
# request=urllib.request.Request(url,data)#post,发起请求，传递data
# res =  urllib.request.urlopen(request)
# print(res.read())

import  requests
import time
import json
mycookie=dict(JSESSIONID="49d1eb7b-663a-4967-ab9c-ecc62c150c53")
req=requests.get("http://cxzhg.gtcx-tech.com",cookies=mycookie)
time.sleep(3)
print(req.cookies)
print(req.text)
print("-------------------------------------------------")
data={"tenantId":0}
data = json.dumps(data)
headers = {

    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding": "gzip,deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive",
    "Content-Length":"14",
    "Content-Type": "application/json",
    "Cookie":"JSESSIONID=49d1eb7b-663a-4967-ab9c-ecc62c150c53",
    "Host": "cxzhg.gtcx-tech.com",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1)AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 38.0.2125.111Safari / 537.36",
    "Referer": "http://cxzhg.gtcx-tech.com/modules/charger/chargeStation.html",
    "X-Requested-With": "XMLHttpRequest", }
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
url="http://cxzhg.gtcx-tech.com/charge/station/list"
mycookie=dict(JSESSIONID="49d1eb7b-663a-4967-ab9c-ecc62c150c53")
req=requests.post(url, data=data,headers=headers,cookies=mycookie)
print(req.text)
#
#coding:utf-8
# import requests
# session=requests.Session()#会话
# #emp_no=admin&password=admin
# params={"emp_no":"admin","password":"admin1"}
# mysession=session.post("http://demo.smeoa.com/index.php?m=&c=public&a=check_login",params)
# print(mysession.cookies.get_dict())
# mysession=session.get("http://demo.smeoa.com")
# print(mysession.text)

# #coding:utf-8
# import requests
# session=requests.Session()#会话
# #emp_no=admin&password=admin
# params={"emp_no":"admin","password":"admin1"}
# mysession=session.post("http://cxzhg.gtcx-tech.com/charge/station/list",params)
# print(mysession.cookies.get_dict())
# mysession=session.get("http://demo.smeoa.com")
# print(mysession.text)