# 생성
d = {'basketball': 5, 'soccer': 11, 'baseball': 9}
print(d, type(d))

# 인덱싱 대신 키 객체으로 검색
print(d['basketball'])
# 없는 키로 검색은 error
# print(d['volleyball'])

# mutable
d['volleyball'] = 6
print(d)

# 길이
print(len(d))

# 확인
print('soccer' in d)
print('volleyball' not in d)

# 다양한 사전생성
d = dict()
print(d)

d = dict(one=1, two=2)
print(d)
d = dict([('three',3), ('four',4)])
print(d)

# 사전 키는 변경 불가능한 타입의 객체여야한다.
d = dict()
d[True] = 'True'
d[10] = 'ten'
d['twenty'] = '20'
d[(1, 2, 3)] = '6'
# 에러
# d[[1, 2, 3]] = '6'
print(d)


# 메서드
keys = d.keys()
print(keys, type(keys))

for key in keys:
    print('{0}:{1}'.format(key, d[key]))


values = d.values()
print(values, type(values))

items = d.items()
print(items, type(items))

for item in items:
    print('{0}:{1}'.format(item[0], item[1]))


for key, value in items:
    print('{0}:{1}'.format(key, value))

# 값 가져오기
d = {'둘리': '010-1111-1111', '마이콜': '010-2222-2222'}
print(d['둘리'])
print(d.get('둘리'))
# 없는 경우 None 대신에 디폴트값 세팅
print(d.get('도우넛', '000-000-0000'))

# 없는 경우에는 데이터를 넣고 가져온다.
print(d.setdefault('도우넛', '000-000-0000'))
print(d)
# 삭제와 동시에 가져오기.
print(d.pop('도우넛'))
print(d)
# 튜플형태로 가져오기
n = d.popitem()
print(n)

# update & clear
d.update({'둘리':'010-2222-2222', '길동':'010-3333-3333'})
print(d)
d.clear()
print(d)

# 사전 순회
d={'c':3, 'a': 1, 'b':2}
for key in d:
    print(key, end=' ')
else:
    print()


for key in d:
    print('{0}:{1}'.format(key, d[key]), end=' ')
else:
    print()

for key in d.keys():
    print('{0}:{1}'.format(key, d[key]), end=' ')
else:
    print()

for key, value in d.items():
    print('{0}:{1}'.format(key, value), end=' ')
else:
    print()


