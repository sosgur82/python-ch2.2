# 한 줄 문자열 정의
s = ''
str1 = 'Hello World'
str2 = 'Hello World'
print(type(s), type(str1))

# 여러줄 문자열 정의
str3 = """ABCDEFG
abcdefg
가나다라마바사
123456789"""
print(str3)

# escape
print('Hello\nWorld\nI\'d Say "hello World"')
print("Hello\nWorld\nI Say \"hello World\"")

#
# sequence 타입이 가지는 공통적 연산
#
str1 = 'Hello World'

# 인덱싱(indexing)
print(str1[0], str1[2], str1[3], sep=',')

# 슬라이싱(slicing)
print(str1[2:5])
print(str1[2:])

#연결(+)
print(str1 + str2)
#TypeError
#print(str1+10)

#반복(*)
print(str1*3)

#len함수
print(len(str1))

#in ,not in 연산
print('S'in str1)
print('S'not in str1)

#변경불가능(immutable)
#str1[0] ='Q'

# formatting
name = "둘리"
age = 20
# print('name:' + name + ",age:" + 20)
print('name:' + name + ",age" + str(20))
print('name:' + format(name, 's') + 'age:' + format(age, 'd'))

u1 = ('둘리', 10)
u2 = ('마이콜', 20)

s = 'name: %s, age:%d'
print(s % u1)
print(s % u2)

# 대소문자 관련 메소드
s = 'i like Python'
print(s.upper())
print(s.lower())
print(s.capitalize())
print(s.title())

# 검색 관련
s = 'I Like Python, I Like Java Also'

print(s.count('Like'))
print(s.find('Like'))
print(s.find('Like', 5))
print(s.rfind('Like'))

#  검색 실패 시
print(s.find('JS'))
# 실패시 예외 발생
# print(s.index('JS'))

print(s.startswith('I Like'))
print(s.startswith('Like', 2))
print(s.endswith('Also'))
print(s.endswith('Java', 0, 26))

# 편집과 치환
s = '    spam and ham    '
print('---' + s.strip() + '----')
print('---' + s.rstrip() + '----')
print('---' + s.lstrip() + '----')

s = '<><abc><><defg><><>'
print(s.strip('<>'))

s = 'Hello Java'
print(s.replace('Java', 'Python'))

# 분리와 결합
s = 'spam and ham'
t = s.replace(' ', '').split('and')
print(t)

t2 = ':'.join(t)
print(t2)

s = "one:two:three:four:five"
print(s.split(":", 2))
print(s.rsplit(":", 1))

lines = """1st line
2nd line
3rd line
4th line
"""
print(lines.splitlines())


# 판별
print('1234'.isdigit())
print('abcd'.isalpha())
print('1234'.isalpha())
print('abcd'.isdigit())

print('abcd'.islower())
print('ABCD'.isupper())

print(''.isspace())
print('\n\n'.isspace())
print('           '.isspace())

# 0로 채우기
print('20'.zfill(5))

# format
f = 'name:{0}, age:{1}'
print(f.format(name, age))
print('name:{1}, age:{0}'.format(age, name))

d = {'name': '마이콜', 'age': 20}
print('name:{name}, age:{age}'.format_map(d))
