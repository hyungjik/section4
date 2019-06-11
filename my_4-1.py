import pickle  # (객체,텍스트) 직렬화, 역직렬화

# 파일 이름과 데이터
bfilename = 'd:/inflearn/crawling/section4/test.bin'
tfilename = 'd:/inflearn/crawling/section4/test.txt'

data1 = 77
data2 = "Hello, world!"
data3 = ['car', 'apple', 'house']

# 바이너리 쓰기
with open(bfilename, 'wb') as f:
    pickle.dump(data1, f)  # dumps(문자열 직렬화)
    pickle.dump(data2, f)
    pickle.dump(data3, f)

# 텍스트 쓰기
with open(tfilename, 'wt') as f:
    f.write(str(data1))
    f.write(str('\n'))
    f.write(data2)
    f.write(str('\n'))
    f.writelines('\n'.join(data3))

# 바이너리 읽기
with open(bfilename, 'rb') as f:
    b = pickle.load(f)  # loads (문자열 역직렬화)
    print(type(b), ' Binary read1 |', b)
    b = pickle.load(f)
    print(type(b), ' Binary read2 |', b)
    b = pickle.load(f)
    print(type(b), ' Binary read2 |', b)

# 텍스트 읽기
with open(tfilename, 'rt') as f:
    for i, line in enumerate(f, 1):
        print(type(line), "Text read" + str(i) + ' |', line, end='')
