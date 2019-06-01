# coding=utf-8
# 今天说一下python的关键字
# 可以通过以下手段查看
import keyword
print(keyword.kwlist)

# 不要随意使用python关键字作为自己定义的类的属性或者方法名。
# 尤其是定义数据库字段的时候，比如 class这个关键字。
# 使用关键字会出现莫名其妙的乱七八糟的错误
