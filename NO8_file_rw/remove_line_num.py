
file_name = 'test.txt'

file_w = open('output.txt', 'w', encoding='utf-8')
lines = open(file_name, 'r', encoding='utf-8').readlines()
file_w.writelines([line[3:] for line in lines])
file_w.close()




