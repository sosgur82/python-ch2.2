# 객체의 값 대소 비교
print(1 > 3)
print(2 > 4)

print(2 >= 4)
print(2 <= 4)

print(2 == 4)
print(2 != 4)

# 복합관계식도 지원
a = 6
print(0 < a and a < 10)
print(0 < a < 10)

# 수치형 이외의 객체도 비교가능
print('abcd' > 'abc')
print([1, 2, 4] > [1, 2, 3, 5])

# 동질(값)성 비교  ==
# 동일(참조값)성 비교  is

a = 10
b = 20
c = 10

print(a == b)
print(a is b)

print(a == c)
print(a is c)

# 논리식의 계산 순서
print([1] or 'logical')
print('logical' and 'operator')
print(None and 1)
