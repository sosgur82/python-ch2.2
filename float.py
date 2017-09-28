# 다른 언어에서처럼 소수점을 포함하거나 e나 E로 지수로 표현할 수 있다.

a = 1.2
print(type(a))
print(isinstance(a, float))
print(a.is_integer())

b = 3e3
print(b)
c = -0.2e-4
print(c)

# is_integer() 는 값이 정수 인지만 판단한다.
b = 3.0
print(b.is_integer())



