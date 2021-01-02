#coding=utf-8
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

def simple_sub():
    str1 = '''
    "<div class="tip">
          面粉的吸水性不一样，多分几次加入，直到揉成<br>柔软的面团即可。<br>奶粉我用孩子喝的Bubs有机奶粉，奶粉有<br>着淡淡的奶香味，奶质也细腻，冲泡出来味道比<br>较清淡，没有结块和挂壁现象，<br>味，宝宝容易接受。奶粉中的益生菌能使我家宝<br>宝更好吸收营养成分，<br>小零食辅食的时候，也会加入奶粉，除了给美食<br>增加一份奶香味之外，也多增加了一份营养健<br>康，宝宝喜欢的不得了~
        </div>"
    '''
    repl = ''
    str1 = re.sub('<div class="tip">', repl, str1)
    str1 = re.sub('</div>', repl, str1)
    str1 = re.sub('<br>', repl, str1)
    str1 = re.sub('\s', repl, str1)
    print(str1)


def update():
    str1 = """
boost 库的官网是 www.boost.org

# 参考
[1]KangRoger的 ec 读书笔记
http://blog.csdn.net/kangroger/category_2771821.html ab"""
    # file_path = '/Users/zxzx/writings/cpp_blog/[读书笔记][EffectiveC++]条款41-模板编程的隐式接口.md'
    # with open(file_path, encoding='utf-8') as f:
    #     str1 = f.read()
    # str1 = " https://www.cnblogs.com/huxi/archive/2010/07/04/1771073.html . "
    str1 += '\n'
    # str1 = "abc abc"
    ret = re.sub("[^\[]([https|http]+://[\.a-zA-Z\?/_0-9]+[^\s])", r'[\1](\1)', str1) # 不能以[开头, 因为这表示替换过的
    # ret = re.sub('(\w.+)', r'\1\1', str1)
    # ret = re.findall('(https://\w.+)', str1)
    print(ret)






if __name__ == '__main__':
    # test_what_is_re_sub_example2()
    # str1 = simple_sub()
    update()