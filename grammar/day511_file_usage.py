# coding=utf-8
# 内置的文件工具怎么使用呢？

# question1: 创建或者打开一个指定名字的文件，并向里面写入一行字符。
text1 = open('file_test.txt', 'a+')
text1.write('你好')  # write并不会换行， 所以后面要加上\n
text1.write('你好\n')
text1.close()

# 生成的文本是：
#   你好你好

# question2: 如果没有close, 写入数据还能保存吗？
text1 = open('file_test2.txt', 'a+')
text1.write('你好')  # write并不会换行， 所以后面要加上\n
# 答案是好像可以，但是还是建议 有close方法。


# 使用with的简洁写法, 不用写close方法。
with open('file_test2.txt', 'a+') as text1:
    text1.write('你好')  # write并不会换行， 所以后面要加上\n