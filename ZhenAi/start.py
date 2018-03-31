from  scrapy import cmdline
#pycharm执行风格
# cmdline.execute(["scrapy","crawl","zhenai"])

import os
os.chdir('ZhenAi/spiders')
cmdline.execute('scrapy runspider zhenai.py'.split())