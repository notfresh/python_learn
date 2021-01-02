g_data = {}
g_dependency = {
    'bannerPath': ['banner',True], # bannerPath 依赖 banner
    'license': ['mit',False],# license 依赖 mit,但是依赖关系相反
    'diffYear': ['currentYear',False] # license 依赖 mit,但是依赖关系相反
}

def validate_name(name):
    return len(name) > 2


def validate_maintainer(maintainer):
    return len(maintainer) > 2


def validate_confirm(value):
    return value in ('y', 'n')


def validate_length(value):
    return len(value) > 0


def filter_confirm(value):
    return value == 'y' #  if y return True, else False


questions = [
    {
        'name': 'moduleName',
        'message': 'What is the name of your module?\n',
        'type': 'input',
        'default': '名称待定',
        'validate': validate_name
    }, {
        'name': 'banner',
        'message': 'Do have a banner image?y/n\n',
        'type': 'confirm',
        'default': 'n'
    }, {
        'name': 'bannerPath',
        'message': 'Where is the banner image? Example: \'img/banner.png\'\n',
        'type': 'input',
        'when': g_data.get('banner', 'n')
    }, {
        'name': 'badge',
        'message': 'Do you want a standard-readme compliant badge?y/n\n',
        'type': 'confirm',
        'default': 'y'
    }, {
        'name': 'badges',
        'message': 'Do you want a TODO dropped where more badges should be?y/n\n',
        'type': 'confirm',
        'default': 'n'
    }, {
        'name': 'longDescription',
        'message': 'Do you want a TODO dropped where your long description should be?y/n\n',
        'type': 'confirm',
        'default': 'n'
    }, {
        'name': 'security',
        'message': 'Do you need a prioritized security section?y/n\n',
        'type': 'confirm',
        'default': 'n'
    }, {
        'name': 'background',
        'message': 'Do you need a background section?y/n\n',
        'type': 'confirm',
        'default': 'n'
    }, {
        'name': 'API',
        'message': 'Do you need an API section?y/n\n',
        'type': 'confirm',
        'default': 'n'
    }, {
        'name': 'maintainers',
        'message': 'What is the GitHub handle of the main maintainer?y/n\n',
        'type': 'input',
        'validate': validate_maintainer
    }, {
        'name': 'contributingFile',
        'message': 'Do you have a CONTRIBUTING.md file?y/n\n',
        'type': 'confirm',
        'default': 'n'
    }, {
        'name': 'prs',
        'message': 'Are PRs accepted?y/n\n',
        'type': 'confirm',
        'default': 'y'
    },
    {
        'name': 'mit',
        'message': 'Is an MIT license OK?y/n\n',
        'type': 'confirm',
        'default': 'y'
    }, {
        'name': 'license',
        'message': 'What is your license?y/n\n',
        'type': 'input',
        'validate': validate_length
    },
    {
        'name': 'licensee',
        'message': 'Who is the License holder (probably your name)?\n',
        'type': 'input',
        'validate': validate_length
    }, {
        'name': 'currentYear',
        'message': 'Use the current year?y/n\n',
        'type': 'confirm',
        'validate': 'y',
    }, {
        'name': 'diffYear',
        'message': 'What years would you like to specify?y/n\n',
        'type': 'input'
    }

]

def depend(name):
    dependency = g_dependency.get(name,[])
    if not dependency: # 没有依赖,返回True
        return True
    if dependency[1]:
        return g_data.get(dependency[0], False)
    else:
        return not g_data.get(dependency[0], False)

def query():
    for quest in questions:
        if quest['type'] == 'input' and depend(quest['name']) :
            while True:
                value = input(quest['message']) or quest.get('default', '')
                if quest.get('validate', False): # 是否需要检测,默认不需要检测
                    flag = quest['validate'](value)
                    if flag: break # 检测是否合法
                    else:
                        print('please check your input value\n')
                else:
                    break
            g_data[quest['name']] = value
        elif quest['type'] == 'confirm' and depend(quest['name']) :
            while True:
                value = input(quest['message']) or quest.get('default', 'y')
                print("get value:",value)
                flag = validate_confirm(value)
                if flag:
                    value = filter_confirm(value) # 检测是否合法
                    break
                else:
                    print('please check your input value\n')
            g_data[quest['name']] = value

    return g_data

if __name__ == '__main__':
    pass


# def title_question(id, answer):
#     if(answer == 'y'):
#         answer1 = input('请输入你的标题')
#     else:
#         answer1 = '默认标题'
#     return answer1
#
# questions = [
#     [1,"你需要标题吗?", title_question],
#     # [2,"你平时喜欢做什么?",""],
#     # [3,"你来自哪里?",""],
# ]

#
# for qst in questions:
#     answer = input(qst[1])
#     answer2 = qst[2](qst[0], answer)
#     print( qst[0], qst[1] ,answer, answer2)
