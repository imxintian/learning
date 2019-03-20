# 猫眼排行 爬取
# baseUrl = https://maoyan.com/board/4
# 分析 : 打开基础URL，发现排名第一的电影是霸王别姬，页面中显示的有效信息有影片名称、主演、上映时间、上映地区、评分、图片等信息
# 而滚动到最后 发现有分页 点击可以发现页面的URL变成http://maoyan.com/board/4?offset=10，比之前的URL多了一个参数，那就是offset=10，
# 而目前显示的结果是排行11~20名的电影，初步推断这是一个偏移量的参数。
# 再点击下一页，发现页面的URL变成了http://maoyan.com/board/4?offset=20，参数offset变成了20，而显示的结果是排行21~30的电影

# 由此可以总结出规律，offset代表偏移量值，如果偏移量为n，则显示的电影序号就是n+1到n+10，每页显示10个。
# 所以，如果想获取TOP100电影，只需要分开请求10次，而10次的offset参数分别设置为0、10、20、…90即可，
# 这样获取不同的页面之后，再用正则表达式提取出相关信息，就可以得到TOP100的所有电影信息了
import json
import re
import time

import requests
from requests import RequestException


def get_one_page(url):
    try:
        headers ={
            'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
        }
        res = requests.get(url, headers=headers)
        if res.status_code == 200:
            return res.text
        return None
    except RequestException:
        return None


def pase_one_page(html):
    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a'
                         + '.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>'
                         + '.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>', re.S)
    items = re.findall(pattern, html)
    for item in items:
        yield {
            'index': item[0],
            'image': item[1],
            'title': item[2],
            'actor': item[3].strip()[3:],
            'time': item[4].strip()[5:],
            'score': item[5]+item[6]

        }


def write_to_file(content):
    with open('result.txt','a',encoding='utf-8') as f:
        f.write(json.dumps(content,ensure_ascii=False)+'\n')


def main(offset):
    url = "https://maoyan.com/board/4?offset="+str(offset)
    html = get_one_page(url)
    for item in pase_one_page(html):
        print(item)
        write_to_file(item)


if __name__ == '__main__':
    for i in range(10):
        main(offset=i*10)
        time.sleep(1)


