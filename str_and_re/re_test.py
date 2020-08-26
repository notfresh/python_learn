import re

#
# the_str = 'I love Peking University , haha'
the_str = 'I love Peking University AXB and i want to go there, How about you?'
words = the_str.split(' ')
length = len(words)
i = 0
while i < length:
    item = words[0]
    j = 0
    while re.match('[A-Z][a-z]+', words[j]):
        j += 1
    if j > 1:
        for k in range(j):
            words.pop(0)
            words.append('NOUN')
        i += j
    else:
        words.pop(0)
        words.append(item)
        i += 1
res = ' '.join(words)
print(res)




# a = "ABc"
# res = re.match('[A-Z][a-z]+', a)
# print(res.group())