matrix = []

for i in range(3):
    row = [] #สร้างไว้เก็บในแถว
    for j in range(3):#ใส่เลขได้3ครั้ง
        row.append(int(input())) # [1,2,3] 
    matrix.append(row) #เก็บไว้ในลิสไว้ในแถว ลูป3รอบ เป็น3แถว3คอลลั้ม ตรงนี้เอาไว้กำหนดขนาดของmetrix


print("List 2D")
for i in range(len(matrix)): # row loop ลูปแถว
    for j in range(len(matrix[i])): # column loop ลูปตัวในแถว #ใช้ j แทน i เพราะมันถ้าใช้iมันจะซ้ำกัน
        print(matrix[i][j], end=" ")
    print()