score_list = [1,2,3,4,5,7,8,9]#แบบนี้คือ1มิติ

matrix = [
    [1,2,3,4],
    [4,5,6,7],
    [7,8,9,10]
]
#แบบนี้คือ2มิติ ดูจากจำนวนวงเลฺ็บที่ซ้อนกัน ถ้าซ้อนอีกขึ้นก็จะเป็น3มิติ 
print(score_list[3]) # print 1D-list
print(matrix[1][2])#[1]บอกแถวว่าตอนนี้แถว2[2]บอกจำนวนตัวในแถวเช่นตอนนี้ แถว2ตัวที่3

print("----------")
for i in range(len(score_list)):
    print(score_list[i])  #ลูปปกติของ1D

#matrix.append([10,11,12])#เพิ่มแถวตามนี้
"""1 2 3 
4 5 6
7 8 9
10 11 12"""
matrix[0].append(11)#เพิ่มตัวในแถว
"""1 2 3 11
4 5 6
7 8 9"""


print("List 2D")
for i in range(len(matrix)): # row loop ลูปแถว
    for j in range(len(matrix[i])): # column loop ลูปตัวในแถว #ใช้ j แทน i เพราะมันถ้าใช้iมันจะซ้ำกัน
        print(matrix[i][j], end=" ")
    print()#พอลูปเสร็จแถวนึงปุ๊ป ก็จะขึ้นบรรทัดใหม่ให้สวยๆเหมือนmatrix











