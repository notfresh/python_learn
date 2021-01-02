from templite import Templite
from question_list import query

if __name__ == '__main__':
    path = "standard-readme-django-cn.template"
    context = query()
    tpl = Templite(path, context)
    ret_txt = tpl.render()
    print(ret_txt)


