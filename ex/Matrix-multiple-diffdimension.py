#ทำ matrix คูณกัน 
#โอเคโจทย์ใหม่คือเราจะรอบรับมิติที่ต่างกันมาคูณกัน โดย1)เราต้องinputค่ามิติ 2 ค่า เพื่อตัวคูณทั้ง2 2)เช็คว่ามิติมันคูณกันได้มั้ย โดยหลักตัวหน้า(colum)ต้องเท่ากับแถวของตัวหลัง(row) 
def creat_metrix(x,y):
    metrix = []
    for i in range (x):
        row = []
        number=input()
        number_split=number.split(" ")
        for j in range (y):
            row.append(int(number_split[j]))
        metrix.append(row)

    return metrix

while True:
    mxn1 = input()
    mxn_split1=mxn1.split(" ")
    mxn2 = input()
    mxn_split2=mxn2.split(" ")
    if mxn_split1[1]==mxn_split2[0]:
        break
    else:
        print("error can't multiply")

x = int(mxn_split1[0])
y = int(mxn_split1[1])
a = int(mxn_split2[0])
b = int(mxn_split2[1])
metrix_one= creat_metrix(x,y)
metrix_two= creat_metrix(a,b)

matrix_result=[]

#โอเคงานหยาบและ ทำไงให้มันคูณกัน เอาแถวแนวนอนบันทัดที่1 คูณกับ แถวที่1แล้วต่อด้วย2 ไม่ดิ คือมันเอาตัวที่หนึ่งคูณกับ
"""
1 2
3 4

3 5
7 2

17 9
37 23"""

"""
A = 3x2
B = 1x3
"""


for i in range (len(metrix_one)): # row
    row = []
    for k in range(len(metrix_two[i])): #ลูปอันนี้เอาไว้วนเลื่อไปแถวด้านข้าง(next colum)ต่อไป ไม่งั้นมันจะลูปโดยไม่ทำcolumข้างๆแล้วก็ขึ้นลูปrowอันใหม่ #ทำไมต้องลูปถ้าไม่ลูปมันจะทำแค่jครั้งเดียวแล้้วมันจะคูณแนวตั้งแค่ครั้งเดียว
        sum = 0 #แล้วก็มีsumเพื่อรับค่า2ตัวที่คูณไขว้กัน
        for j in range(len(metrix_two[i])):
            sum += metrix_one[i][j] * metrix_two[j][k] #<--เหตุผลที่ใช้kก็เพราะถ้าใช้iมันจะค้างอยู่ที่ตำแหน่งที่0เพราะมันลูปแค่นั้น แต่ถ้าkมันจะเลื่อนไปตำแหน่งข้างๆอันต่อไป#มันจะคูณไขว้กัน ไม่เชื่อดูได้ตามmatrixที่เค้าเขียนในเน็ตตำแหน่งมันจะสลับกัน
        row.append(sum)
    matrix_result.append(row)

#เผื่อมึงงง บีม คือ แบบลูปปกติมันก็คูณแถวแรกกับแนวตั้งอีกอัน 1 2 เจอกับ 3 7  แล้วจากนั้น มันก็จะขึ้นแถวใหม่เป็น 1 2 เจอกับ 3 7 ทันที เพราะงั้นมันเลยเจ๊ง
#มึงเลยต้องมีkเพื่อstopว่าเห้ยก่อนมึงไปต่อ ต้องอ่านด้านข้างคือ 5 2 ก่อนไอหนู เลยเป็น k แทน i ในบรรทัดที่40 แทน ซึ่งk ทำหน้าที่อ่านจำนวนตัวในแนวนอน okพอเก็ทนะ
#เพิ่มเติม sum += เพราะ ปกติ matrix คูณก่อนแล้วค่อยบวก มันก็เลยเก็บพร้อมบวกค่าก่อนหน้า ไว้ในsum จากนั้นพอหมดลูปก็เพิ่มในrowทีละตัวจนครบตามที่มิติมันเก็บได้
#ยังไงนะที่พิมเค้าสั่ง คือเอา rowใส่ในmatrix result แล้วปริ้นออกมาสวยๆ 

for i in range (len(matrix_result)):
    for j in range (len(matrix_result[i])):
        print(matrix_result[i][j], end=" ")
    print()
    








