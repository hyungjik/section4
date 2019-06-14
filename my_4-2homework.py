from bs4 import BeautifulSoup
import urllib.request as req
import os.path
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

# 과제내용 : 시간대별로 최고온도와 최저온도를 출력 txt 파일로

# 다운로드 url
url = "http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=1132067000"
savename = "D:/inflearn/crawling/section4/4_2/homework_forecast.xml"

if not os.path.exists(savename):
    req.urlretrieve(url, savename)
    print("다운로드 완료!")

# BeautifulSoup 파싱
xml = open(savename, 'r', encoding="utf-8").read()
soup = BeautifulSoup(xml, "html.parser")  # html 태그기 때문에 html파서씀ㅋ

# day 확인
info = {}
for day in soup.find_all("data"):  # xml을 사용할떈 find_all이 좋다
    days = day.find("day").string
    # print(days)
    high_temps = day.find("tmx")
    low_temps = day.find("tmn")
    hours = day.find("hour")
    # print(low_temps)
    if not (days in info):  # info라는 딕셔러니에 key인 loc이 없으면 --> 중복방지
        info[days] = []
        info[days] = []
    for tmx in high_temps:
        info[days].append('high '+tmx.string)
    for tmn in low_temps:
        info[days].append('low '+tmn.string)
print(info)
# print(sorted(info.keys()))  # ㄱ부터 밖에 안됨
# print(list(info.keys()))
# print(info.values())
#
# # 각 지역별 날씨 텍스트 쓰기
# with open("D:/inflearn/crawling/section4/4_2/homework_forecast.txt", 'wt') as f:
#     for loc in sorted(info.keys()):
#         print("+", loc)
#         f.write(str(loc)+'\n')
#         for n in info[loc]:
#             print("-", n)
#             f.write('\t'+str(n)+'\n')
