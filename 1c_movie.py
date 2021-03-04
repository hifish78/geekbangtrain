import requests
# lxml是beautifulsoup的替代库
import lxml.etree

# 爬取页面详细信息

# 电影详细页面
url = 'https://movie.douban.com/subject/1292052/'

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'

# 声明为字典使用字典的语法赋值
header = {}
header['user-agent'] = user_agent
response = requests.get(url, headers=header)

# xml化处理
selector = lxml.etree.HTML(response.text)

# 电影名称
film_name = selector.xpath('//*[@id="content"]/h1/span[1]/text()')
print(f'电影名称: {film_name}')

# 上映日期
# 从浏览器里得到的XPATH： //*[@id="info"]/span[10]； 这里多出了text()
plan_date = selector.xpath('//*[@id="info"]/span[10]/text()')
print(f'上映日期: {plan_date}')

# 评分
rating = selector.xpath('//*[@id="interest_sectl"]/div[1]/div[2]/strong/text()')
print(f'评分：{rating}')

mylist = [film_name, plan_date, rating]

# 把从浏览器得到的信息保存
import pandas as pd

movie1 = pd.DataFrame(data = mylist)

# windows需要使用gbk字符集
movie1.to_csv('./movie1.csv', encoding='utf8', index=False, header=False)

