#논리연산자
a = 20
b = 30

print(not a > b)
print(a < b and a != b)
print(a == b or a > b)

#True -> 1, False -> 0
print(True+1)
print((a>b)+1)

#캐스팅
b = bool(10)
print(b, type(b))
print(bool(None))
