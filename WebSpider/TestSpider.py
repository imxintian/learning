# import urllib.request
#
# from urllib.parse import urlparse
# data = bytes(urllib.parse.urlencode({"key": "value"}),encoding='utf8')
# print(data)
# response = urllib.request.urlopen('http://httpbin.org/post', data=data)
#
# result = urlparse('https://www.baidu.com/index.html;user?id=5#12')
# print(type(result), result)
#
import requests


r = requests.get('https://www.baidu.com')

# print(type(r))
# print(r.text)


