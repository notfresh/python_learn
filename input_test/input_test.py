def title_question(id, answer):
    if(answer == 'y'):
        answer1 = input('请输入你的标题')
    else:
        answer1 = '默认标题'
    return answer1

questions = [ # @question
    [1,"你需要标题吗?", title_question],
    # [2,"你平时喜欢做什么?",""],
    # [3,"你来自哪里?",""],
]


for qst in questions:
    answer = input(qst[1])
    answer2 = qst[2](qst[0], answer)
    print( qst[0], qst[1] ,answer, answer2)




