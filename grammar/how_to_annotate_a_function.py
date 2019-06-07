# coding=utf-8
# 如何给一个方法写注释呢？
# 我没尝试过手动写， 使用pycharm的懒办法手动生成吧。

# 例如：

def f1(x, y):
    """

    :param x:
    :param y:
    :return:
    """
    return x + y

# 我是怎么做到的呢？
# 在pycharm中， 在方法的第一行， 输入三个双引号， 然后点回车（enter键），pycharm就会自动生成对参数的注释
# 另外再提两点：
#    在python中，方法的第一行的字符串是无效的，python编译器会认为这个字符串就是注释。
#    3个引号的字符串是可以跨行的。