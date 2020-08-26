import re


# re.sub方法是什么?
def test_what_is_re_sub():
    str1 = r"17600001234"
    regex = r"(\d{3})(\d{4})(\d{4})"
    result = re.sub(regex, r'\1****\3', str1)
    print(type(result))
    print(result)

    '''
    output:
        <class 'str'>
        176****1234
    说明:
    对sub的解释是:
        sub是substitute的缩写.
        sub是对 str.replace(old, new)的一种强化. 在str1里面寻找符合regex格式的局部字符串, 找到后,进行替换操作.
        sub最强的一点是, 可以通过 () 来进行分组. 进而在替换的过程中引用匹配到的分组结果, 动态替换, 功能非常的强大!!
        上面的电话号码遮罩就是一个很经典的案例.
    sub应用场景:
        普通替换, 动态替换       
    '''


def test_what_is_re_sub_example2():
    str1 = r"hello python, 我爱学习"
    regex = r"(\w+) (\w+)"
    result = re.sub(regex, r'\2 AAA \1', str1)
    print(type(result))
    print(result)
    '''
    output:
        <class 'str'>
        python AAA hello, 我爱学习
    '''


if __name__ == '__main__':
    test_what_is_re_sub_example2()