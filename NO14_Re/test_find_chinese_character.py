#coding=utf-8

a = "nihao"
b = "你"
c = 'a'

print(ascii(b))
print(type(ascii(a)))
# ascii_ = ascii(a)
# for item in ascii_:
#     print(item)
#
# ascii_ = ascii(b)
# for item in ascii_:
#     print(item)

ascii_ = ascii(c)
for item in ascii_:
    print(item)


def is_ascii(c):
    return ascii(c)[1:-1] == c

print( is_ascii('a'))
print( is_ascii('0'))
print( is_ascii('我'))
print( is_ascii('('))
print( is_ascii('/'))