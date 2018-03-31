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
# start_url = 'http://search.zhenai.com/v2/search/getPinterestData.do?'
start_url = 'http://search.zhenai.com/v2/search/getPinterestData.do?sex=1&agebegin=18&ageend=18&workcityprovince=10102000&workcitycity=10102001&h1=-1&h2=-1&salaryBegin=-1&salaryEnd=-1&occupation=-1&h=-1&c=-1&workcityprovince1=-1&workcitycity1=-1&constellation=-1&animals=-1&stock=-1&belief=-1&condition=66&orderby=hpf&hotIndex=&online=&currentpage=1&topSearch=false'
# start_url = 'http://search.zhenai.com/v2/search/getPinterestData.do?sex=1&agebegin=18&ageend=21&workcityprovince=10101000&workcitycity=10101201&marriage=1&education=5&h1=-1&h2=-1&salaryBegin=-1&salaryEnd=-1&occupation=-1&h=-1&c=-1&workcityprovince1=-1&workcitycity1=-1&constellation=-1&animals=-1&stock=-1&belief=-1&condition=66&orderby=hpf&hotIndex=&online=&currentpage=1&topSearch=true'
# cookies = {
#     "sid": "J0tRDiGwk3HtkVczaRVo",
#     "Hm_lvt_2c8ad67df9e787ad29dbd54ee608f5d2": "1521632628",
#     "ipCityCode": "10101201",
#     "ipOfflineCityCode": "10101201",
#     "p": "%5E%7Eworkcity%3D10101206%5E%7Elh%3D108012000%5E%7Esex%3D0%5E%7Enickname%3D%E4%BC%9A%E5%91%98108012000%5E%7Emt%3D1%5E%7Eage%3D22%5E%7Edby%3D3d0bd12418367a52%5E%7E",
#     "isSignOut": "%5E%7ElastLoginActionTime%3D1521634038787%5E%7E",
#     "mid": "%5E%7Emid%3D108012000%5E%7E",
#     "loginactiontime": "%5E%7Eloginactiontime%3D1521634038787%5E%7E",
#     "logininfo": "%5E%7Elogininfo%3D15177519557%5E%7E",
#     "live800": "%5E%7EisOfflineCity%3Dtrue%5E%7EinfoValue%3DuserId%253D108012000%2526name%253D108012000%2526memo%253D%5E%7E",
#     "preLG_108012000": "2018-03-21+19%3A47%3A00",
#     "login_health": "6d799c230916d7e90df4bf643a95e1fa3e19366c25ffa9c672391aae7ad1a4f540d3529abaf6e7aa42ad01fc2ecaaf5db0e644bc9b3d7f7a7d0cced48bae01aa",
#     "dgpw": "0",
#     "JSESSIONID": "abc15s3YPISd95qhnDijw",
#     "__xsptplusUT_14": "1",
#     "Hm_lpvt_2c8ad67df9e787ad29dbd54ee608f5d2": "1521634740",
#     "__xsptplus14": "14.1.1521634036.1521634739.2%234%7C%7C%7C%7C%7C%23%236tNhDhxN6kMdP_9tD9HyrUlzfaNON65T%23"
# }
headers = {

    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding": "gzip,deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive",
    "Content-Type": "application/json",
    "Host": "search.zhenai.com",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1)AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 38.0.2125.111Safari / 537.36",
    "Referer": "http://search.zhenai.com/v2/search/pinterest.do",
    "X-Requested-With": "XMLHttpRequest", }
cookies = {
    "sid": "J0tRDiGwk3HtkVczaRVo",
    "Hm_lvt_2c8ad67df9e787ad29dbd54ee608f5d2": "1521632628",
    "ipCityCode": "10101201",
    "ipOfflineCityCode": "10101201",
    "p": "%5E%7Eworkcity%3D10101206%5E%7Elh%3D108012000%5E%7Esex%3D0%5E%7Enickname%3D%E4%BC%9A%E5%91%98108012000%5E%7Emt%3D1%5E%7Eage%3D22%5E%7Edby%3D3d0bd12418367a52%5E%7E",
    "isSignOut": "%5E%7ElastLoginActionTime%3D1521634038787%5E%7E",
    "mid": "%5E%7Emid%3D108012000%5E%7E",
    "loginactiontime": "%5E%7Eloginactiontime%3D1521634038787%5E%7E",
    "logininfo": "%5E%7Elogininfo%3D15177519557%5E%7E",
    "live800": "%5E%7EisOfflineCity%3Dtrue%5E%7EinfoValue%3DuserId%253D108012000%2526name%253D108012000%2526memo%253D%5E%7E",
    "preLG_108012000": "2018-03-21+19%3A47%3A00",
    "login_health": "6d799c230916d7e90df4bf643a95e1fa3e19366c25ffa9c672391aae7ad1a4f540d3529abaf6e7aa42ad01fc2ecaaf5db0e644bc9b3d7f7a7d0cced48bae01aa",
    "dgpw": "0",
    "JSESSIONID": "abc15s3YPISd95qhnDijw",
    "__xsptplusUT_14": "1",
    "Hm_lpvt_2c8ad67df9e787ad29dbd54ee608f5d2": "1521634740",
    "__xsptplus14": "14.1.1521634036.1521634739.2%234%7C%7C%7C%7C%7C%23%236tNhDhxN6kMdP_9tD9HyrUlzfaNON65T%23"
}

data = {"sex":"1",
"agebegin": "18",
"ageend": "21",
"workcityprovince": "10101000",
"workcitycity": "10101201",
"marriage": "1",
"education": "5",
"h1": "-1",
"h2":" -1",
"salaryBegin":" -1",
"salaryEnd":" -1",
"occupation":" -1",
"h": "-1",
"c": "-1",
"workcityprovince1":" -1",
"workcitycity1":"-1",
"constellation":" -1",
"animals": "-1",
"stock": "-1",
"belief": "-1",
"condition": "66",
"orderby": "hpf",
"hotIndex":"",
"online": "",
"currentpage": "1",
"topSearch": "true"}
response = requests.get(url=start_url,headers=headers,cookies=cookies)
# print(res.text.encode("utf-8"))
with open("5.html",'wb+') as f:
    f.write(response.content)
print(response.content)
print(response.text)
print(response.status_code)
print(response.url)
# data = json.loads(response.content)
# data = data['data']
# print('-----------data-------------------------')
# print(data)