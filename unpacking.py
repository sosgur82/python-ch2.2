# packing 은 tuple만 가능
t=10, 20, 30, 'python'
print(t, type(t))

# unpacking tuple
a, b, c, d = t
print(a,b,c,d)

# unpacking error
#a,b={10,20,30,40}

#unpacking extended
a, *b = (1,2,3,4,5)
print(a)
print(b)

*a, b = (1,2,3,4,5)
print(a)
print(b)

a, *b, c = (1,2,3,4,5)
print(a)
print(b)
print(c)