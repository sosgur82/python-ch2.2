# 슬라이싱 테스트
# [시작옵셋:끝옵셋]
# 옵셋은 생략 가능

a = 'abcdef'

# 시작위치 와 끝위치 사이를 짤라내는 거
print(a[1:3])

# 1부터 끝까지..
print(a[1:])

# 처음부터 끝까지
print(a[:])

#범위를 넘어서면 범위내 값으로 조정된다.
print(a[-100:100])

#맨 오른쪽 값을 제외하고
print(a[:-1])

#맨 오른쪽 두개 값을 제외하고
print(a[:-2])

#확장슬라이싱
#[start : stop:step]
a='daskjdlajsdlkjasldjaskldjlas'
print(a[::2])
print(a[10:20:3])

# 거꾸로
print(a[::-1])







