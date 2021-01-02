import re


# re.find_all方法是什么?
def test_what_is_re_findall():
    str1 = r"afiouwehrfui chuxiuhong@hit.edu.cn askdjhfiosueh chuxiuhong@hit.edu.cn asdfad chuxiuhong@hit.edu.cn"
    regex = r"([a-zA-Z]+@hit\.edu\.cn)"
    pattern1 = re.compile(regex)
    result = pattern1.findall(str1)
    print(type(result))
    print(result)
    '''
    output:
        <class 'list'>
        ['chuxiuhong@hit.edu.cn']
    说明:
    对match的解释是:
        str1不动, 使用 regex 去从str1的开始位置,一个字符一个字符的比对, 看str1里面到底包含了多少个regex?
        结果说明只包含一个.
    find_all的应用场景:
        在一个长串里面找是否有想要的信息. 类似于在一段文字里找是否有自己想要的文字. 类似于  a in b判断.并且能返回结果.
    
    '''






if __name__ == '__main__':
    test_what_is_re_findall()