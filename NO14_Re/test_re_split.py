import re


# re.split方法是什么?
def test_what_is_re_split():
    str1 = r"我爱天安门123我爱北京456我爱祖国789"
    regex = r"\d{3}"
    result = re.split(regex, str1)
    print(type(result))
    print(result)

    '''
    output:
        <class 'list'>
        ['我爱天安门', '我爱北京', '我爱祖国', '']
    说明:
    对split的解释是:
         search是对 seperator.split(str1)的推广, 对原有字符串分割的强化.
    split应用场景:
       增强分割字符串 
    '''


if __name__ == '__main__':
    test_what_is_re_split()