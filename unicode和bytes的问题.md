
# 清楚展示什么是unicode， 什么是bytes

```python
msg= b'\u8bbe\u7f6e\u6d41\u91cf\u5f15\u64ce\u76d1\u63a7\u7f51\u5361\u5931\u8d25'

msg_u= '\u8bbe\u7f6e\u6d41\u91cf\u5f15\u64ce\u76d1\u63a7\u7f51\u5361\u5931\u8d25'
msg_u2= u'\u8bbe\u7f6e\u6d41\u91cf\u5f15\u64ce\u76d1\u63a7\u7f51\u5361\u5931\u8d25'


print(msg.decode('unicode_escape'))

print(type(msg))
print(type(msg_u))
print(type(msg_u2))
```
