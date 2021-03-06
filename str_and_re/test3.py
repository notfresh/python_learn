# 美团 2020春招 技术综合试卷在线考试
# 编程题|20.0分3/5
# 最近的避难所
# 时间限制：C/C++语言 1000MS；其他语言 3000MS
# 内存限制：C/C++语言 65536KB；其他语言 589824KB
# 题目描述：
# 由于天灾，人们建立了n个避难所，分别标号为1-n。为了防止拥挤，人们只能从标号为 i 的避难所到达编号为i+1的避难所。
#
# 现在，有以下事件可能出现：
#
# 1.一个避难所被天灾摧毁
#
# 2.一个人在某位置发出求救信号，希望知道自己能去到的最近的避难所编号。
#
# 你需要对于每一次求救信号，输出答案。如果不存在这样的避难所，输出-1。
#
# 输入
# 第一行两个数n，m，代表避难所个数和事件个数。
#
# 接下来m行，每行两个数op，pos。
#
# 若op=1，代表第pos个避难所被摧毁。这个避难所有可能在这次事件之前被摧毁过。
#
# 若op=2，代表有一个人在pos号避难所发出信号。第pos号避难所有可能已经被摧毁过。
#
# 输出
# 对于每一次询问，输出最近的避难所标号。
#
#
# 样例输入
# 4 5
# 2 4
# 1 3
# 2 3
# 1 4
# 2 3
# 样例输出
# 4
# 4
# -1
#
# 提示
# 1≤m≤100000 , 1≤n≤1000000000

