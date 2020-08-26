import re


# re.match方法是什么?
def test_what_is_re_match():
    str1 = r"hello. hello. world"
    regex = r"hello"
    result = re.match(regex, str1)
    print(type(result))
    print(result)
    print(result.group())

    '''
    output:
        <class '_sre.SRE_Match'>
        <_sre.SRE_Match object; span=(0, 5), match='hello'>
        hello
    说明:
        str1要和regex完全风格一致.
    对match的解释是:
        用str1去和regex一一比对, 
        如果 regex先结束, 而str1还没完, 则OK. 说明str1符合regex的格式.
        如果str1一开始就不符合regex的规则, 那么就失败了.
    match应用场景:
        电话号码校验. 先指定一个电话号码的模板, 然后根据传入的电话号码和这个模板比对, 看传入的电话号码是否符合模板.
        邮箱, 身份证等等的校验.
    '''


# 限制首尾的严格校验, 要求str1和regex完全格式一致, 这个测试会失败.
def test_what_is_re_match_plus():
    str1 = r"hello. hello. world"
    regex = r"^world$"
    result = re.match(regex, str1)
    print(type(result))
    print(result)
    print(result.group())


if __name__ == '__main__':
    test_what_is_re_match()