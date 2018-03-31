# -*- coding: utf-8 -*-
import scrapy
import json
from ZhenAi.items import ZhenaiItem
from scrapy.http import Request
from lxml import etree
from scrapy_redis.spiders import RedisSpider
import hashlib
import re
class ZhenaiSpider(RedisSpider):
    name = 'zhenai'
    allowed_domains = ['search.zhenai.com','album.zhenai.com']
    # start_urls = ['http://search.zhenai.com/']
    redis_key = 'zhenai:start_urls'
    url = 'http://search.zhenai.com/v2/searc' \
          'h/getPinterestData.do?sex=1&agebegin=18&ageend=21&' \
          'workcityprovince=10101000&workcitycity=10101201&marriage=1&education=5&h1=-1&h2=-1&' \
          'salaryBegin=-1&salaryEnd=-1&occupation=-1&h=-1&c=-1&workcityprovince1=-1&' \
          'workcitycity1=-1&constellation=-1&animals=-1&stock=-1&belief=-1&condition=66' \
          '&orderby=hpf&hotIndex=&online=&currentpage=1&topSearch=true'
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
    headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Encoding": "gzip,deflate",
            "Accept-Language": "en-US,en;q=0.8,zh-TW;q=0.6,zh;q=0.4",
            "Connection": "keep-alive",
            "Host":"search.zhenai.com",
            # "Content-Type": " application/x-www-form-urlencoded; charset=UTF- 8",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1)AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 38.0.2125.111Safari / 537.36",
            "Referer": "http://search.zhenai.com/v2/search/pinterest.do",
            "X-Requested-With":"XMLHttpRequest"}

    def parse(self, response):
        start_url = 'http://search.zhenai.com/v2/search/pinterest.do'
        # 发起请求获取页面搜索条件
        yield scrapy.Request(url=start_url, callback=self.parse_start, headers=self.headers)

        # 解析搜索首页的处理
    def parse_start(self, response):
        html = response.body.decode('gbk')
        # print(html)

        sex_list = ['1']
        age_list = range(18, 19)
        province = {}
        # {'10102001' : ['10102001', '10102002', '10102005', '10102006', '10102007', '10102008', '10102009', '10102010', '10102011', '10102012', '10102013', '10102014', '10102015', '10102016', '10102017', '10102018']}
        with open('city.html', 'r',encoding='utf-8') as f:
            html = etree.HTML(f.read())
            city_div = html.xpath('//div[@class="city_box"]')
            for city in city_div:
                city_id_list = city.xpath('.//a/@v')
                province_id = city_id_list[0][:-2] + '00'
                province[str(province_id)] = city_id_list

        for key, value in province.items():
            print("-----------------key和value----------")
            print(key, value)


        base_url = 'http://search.zhenai.com/v2/search/getPinterestData.do?sex=%s&agebegin=%s&ageend=%s&workcityprovince=%s&workcitycity=%s&h1=-1&h2=-1&salaryBegin=-1&salaryEnd=-1&occupation=-1&h=-1&c=-1&workcityprovince1=-1&workcitycity1=-1&constellation=-1&animals=-1&stock=-1&belief=-1&condition=66&orderby=hpf&hotIndex=&online=&currentpage=%s&topSearch=false'

        for sex in sex_list:
            for age in age_list:
                for proid, city_list in province.items():
                    for cityid in city_list:
                        for page in range(1, 2):
                            print(sex, age, proid, cityid, page)

                            fullurl = base_url % (str(sex), str(age), str(age), str(proid), str(cityid), str(page))
                            # print("-----------------------fullurl-------------------------------")
                            # print("-----------------------fullurl-------------------------------")
                            # print(fullurl)
                            yield scrapy.Request(fullurl, callback=self.parse_list, headers=self.headers,
                                                 cookies=self.cookies)

    def parse_list(self, response):
        print("----------------------------body--------------------------")
        print("----------------------------body--------------------------")
        print("----------------------------body--------------------------")

        print(response.body)
        data = json.loads(response.body.decode('gbk'))
        data = data['data']
        print('-----------data-------------------------')
        print(data)
        base_url = 'http://album.zhenai.com/u/%s'
        # 生成详情请求
        for item in data:
            memberid = item['memberId']
            fullurl = base_url % memberid
            # priority 设置请求在队里的优先级
            yield scrapy.Request(url=fullurl, callback=self.parse_detail, headers=self.headers, cookies=self.cookies,
                                 priority=1)

        # 处理详情页

    def parse_detail(self, response):
        # print response.body.decode('gbk')
        # 提取详情页数据，组建item
        item = ZhenaiItem()
        nick = response.xpath('//a[@class="name fs24"]/text()').extract()[0]
        age = response.xpath('//table[@class="brief-table"]//tr[1]/td[1]/text()').extract()[0]
        age = re.search(r'\d+', age).group()

        item['nick'] = nick
        item['age'] = age
        item['url'] = self.md5(response.url)
        # yield item
        print('生成item')
        yield item

    def md5(self, data):
        m = hashlib.md5()
        m.update(data.encode('utf8'))
        return m.hexdigest()
