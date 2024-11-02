"""
    Enter score: 73

    Grade 4 = 3
    Grade 3.5 = 2
    Grade 3 = ?
    Grade 2.5 = ?
    Grade 2 = ?
    Grade 1.5 = ?
    Grade 1 = ?
    Grade 0 = ?
"""
count_grade = {"0": 0, "1":0, "1.5":0, "2":0, "2.5":0, "3":0, "3.5":0, "4":0}

while True:
    score=eval(input("score (Key -1 to exit):"))
    if score == -1:
        break
    if score>120 or score<0:
        print("ERROR")
    elif score>=80:
        count_grade["4"] = count_grade["4"]+1
    elif score>=75:
        count_grade["3.5"] = count_grade["3.5"]+1
    elif score>=70:
        count_grade["3"] = count_grade["3"]+1
    elif score>=65:
        count_grade["2.5"] = count_grade["2.5"]+1
    elif score>=60:
        count_grade["2"] = count_grade["2"]+1
    elif score>=55:
        count_grade["1.5"] = count_grade["1.5"]+1
    elif score>=50:
        count_grade["1"] = count_grade["1"]+1
    elif score>=0:
        count_grade["0"] = count_grade["0"]+1

for key in count_grade:
    print(f"Grade {key} = {count_grade[key]}")













