grade = int(input("输入成绩\n"))

if (97 <= grade <= 100):
    print(4.0, "A+")
elif (95 <= grade <= 96):
    print(4.0, "A")
elif (grade >= 90 and grade <= 94):
    print(3.7, "A-")
elif (grade >= 85 and grade <= 89):
    print(3.3, "B+")
elif (grade >= 80 and grade <= 84):
    print(2.7, "B")
elif (grade >= 77 and grade <= 79):
    print(2.3, "B-")
elif (grade >= 73 and grade <= 76):
    print(2.0, "C+")
elif (grade >= 70 and grade <= 72):
    print(1.7, "C")
elif (grade >= 67 and grade <= 69):
    print(1.7, "C-")
elif (grade >= 63 and grade <= 66):
    print(1.3, "D+")
elif (grade >= 60 and grade <= 62):
    print(1.0, "D")
elif (grade >= 0 and grade <= 59):
    print(0, "F")










