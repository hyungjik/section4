import simplejson as json
# import json

# Dict(Json) 선언

data = {}
data['people'] = []
data['people'].append({
    'name': 'kim',
    'website': 'naver.com',
    'from': 'Seoul'
})

data['people'].append({
    'name': 'Park',
    'website': 'google.com',
    'from': 'Busan'
})

data['people'].append({
    'name': 'Lee',
    'website': 'daum.net',
    'from': 'Incheon'
})
# print(data)

# Dict(Json) -> str 로 출력해야 파일로 쓸수있다. 직렬화를 해야해

e = json.dumps(data, indent=4)  # 그냥 data를 print하면 dict고 이건 str
# print(type(e))
# print(e)

# str -> dict(json)  이떄는 load로
d = json.loads(e)
# print(type(d))
# print(d)

with open('c:/section4/member.json', 'w') as outfile:
    outfile.write(e)

with open('c:/section4/member.json', 'r') as infile:
    r = json.loads(infile.read())
    print("=====")
    # print(type(r))
    # print(r)
    for p in r['people']:
        print('Name: ' + p['name'])
        print('Website: ' + p['website'])
        print('From: ' + p['from'])
        print("")
