age_A = int(25)
age_Aguess = int(input('请猜测A的年龄？')) # 第一次

if age_Aguess == age_A :
    print('congratulations!!!')
elif age_Aguess > age_A :
    age_Aguess = int(input('猜大了 try again')) # 第二次

    if age_Aguess == age_A:
        print('congratulations!!!')
    elif age_Aguess > age_A:
        age_Aguess = int(input('猜大了 try again')) # 第三次

        if age_Aguess == age_A:
            print('congratulations!!!')
        elif age_Aguess > age_A:
            print("猜大了，游戏结束")

        else:
            print("猜小了，游戏结束")
    else:
        age_Aguess = int(input('猜小了，try again'))  # 第三次
        if age_Aguess == age_A:
            print('congratulations!!!')
        elif age_Aguess > age_A:
            print("猜大了，游戏结束")
        else:
            print("猜小了，游戏结束")
else  :
    age_Aguess = int(input('猜大了 try again'))  # 第二次

    if age_Aguess == age_A:
        print('congratulations!!!')
    elif age_Aguess > age_A:
        age_Aguess = int(input('猜大了 try again'))  # 第三次
        if age_Aguess == age_A:
            print('congratulations!!!')
        elif age_Aguess > age_A:
            print("猜大了，游戏结束")
        else:
            print("猜小了，游戏结束")
    else:
        age_Aguess = int(input('猜小了，try again')) # 第三次
        if age_Aguess == age_A:
            print('congratulations!!!')
        elif age_Aguess > age_A:
            print("猜大了，游戏结束")
        else:
            print("猜小了，游戏结束")


