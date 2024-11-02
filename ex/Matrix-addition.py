#บวกเมทริกซ์ 2 เมทริกซ์ มิติ m × n จากที่โจทย์ระบุให้
#1)input เพื่อกำหนดขนาดmetrix 2)มันต้องเก็บค่า2/3ตัว 3)เราอาจจะต้องทำให้มันรับค่าส่งไปที่ตัวxกับyเพื่อกำหนดขนาดmetrixแล้วก็4)ทำเป็นฟังช์ชั้นเพื่อให้มันทำงานซ้ำได้แบบส่งค่าให้2metrix5)แล้วเราก็ต้องทำลูปแต่ละตัวของเมทริก1และ2มาบวกกัน 6)เก็บค่าที่บวกได้ในเมทริกใหม่


def create_metrix(x,y): 
    metrix = []
    for i in range(x):
        row = []
        number=input()
        number_split=number.split(" ") 
        for j in range(y):
            row.append(int(number_split[j]))
        metrix.append(row)
        
    
    return metrix

mxn= input()
mxn_split=mxn.split(" ") # ["2", "2"]
x = int(mxn_split[0])
y = int(mxn_split[1])
metrix_one=create_metrix(x,y)
metrix_two=create_metrix(x,y)

matrix_result=[]

for i in range(len(metrix_one)):
    row = []
    for j in range(len(metrix_one[i])):
        row.append(metrix_one[i][j] + metrix_two[i][j])
    matrix_result.append(row)

               

for i in range(len(matrix_result)):
    for j in range(len(metrix_one[i])):
        print(matrix_result[i][j], end=" ")
    print()

"""
1 2
3 4
3 5
7 2

17 9
37 23

"""