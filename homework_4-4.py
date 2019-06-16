import urllib.request as req
import os.path, random
import simplejson as json

# URL
url = "https://jsonplaceholder.typicode.com/posts"

# 경로 & 파일명
savename = "d:/inflearn/crawling/section4/placeholder.json"

if not os.path.exists(savename):
    req.urlretrieve(url, savename)
    print('complete download!')

items = json.load(open(savename, 'r', encoding='utf-8'))
# # items = json.loads(open(savename, 'r', encoding='utf=8').read())

# 출력
for item in items:
    print(str(item["id"]) + "   -   " + item["title"])
