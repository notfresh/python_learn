from templite import Templite

if __name__ == '__main__':
    """
# {{title}}
这是标题啊

# 目录
"""
    template = """
# 目录    
{% for item in contents %}
- {{ item }}
{% endfor %}  


{% for item in contents %}
- {{ item }}
{% endfor %}  
    """
    tpl = Templite(template)
    ret_txt = tpl.render({
        'title': "测试",
        'contents': ['a', 'b', 'c']
    })
    print(ret_txt)

