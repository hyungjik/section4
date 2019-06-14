from bs4 import BeautifulSoup
import urllib.request as req
import os.path
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

# 다운로드 url
url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108"
savename = "D:/inflearn/crawling/section4/4_2/forecast.xml"

if not os.path.exists(savename):
    req.urlretrieve(url, savename)
    print("다운로드 완료!")

# BeautifulSoup 파싱
xml = open(savename, 'r', encoding="utf-8").read()
soup = BeautifulSoup(xml, "html.parser")  # html 태그기 때문에 html파서씀ㅋ

# 지역 확인
info = {}
for location in soup.find_all("location"):  # xml을 사용할떈 find_all이 좋다
    loc = location.find("city").string
    # print(loc)
    weather = location.find_all("tmn")
    # print(weather)
    if not (loc in info):  # info라는 딕셔러니에 key인 loc이 없으면 --> 중복방지
        info[loc] = []
    for tmn in weather:
        info[loc].append(tmn.string)
print(info)
# print(sorted(info.keys()))  # ㄱ부터 밖에 안됨
# print(list(info.keys()))
# print(info.values())

# 각 지역별 날씨 텍스트 쓰기
# with open("D:/inflearn/crawling/section4/4_2/forecast.txt", 'wt') as f:
#     for loc in sorted(info.keys()):
#         print("+", loc)
#         f.write(str(loc)+'\n')
#         for n in info[loc]:
#             print("-", n)
#             f.write('\t'+str(n)+'\n')
