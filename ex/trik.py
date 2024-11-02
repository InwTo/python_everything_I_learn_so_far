#จงเขียนโปรแกรมเพื่อรับรหัสการเคลื่อนย้ายแก้ว และหาตำแหน่งสุดท้ายของลูกบอล
#ขั้นแรกเราก็ต้องทำa b c เป็นpatternของการสลับ 1 2 3 คือแก้วแต่ละใบที่โดนสลับและต่ำแหน่งของแก้ว
#1)ทำอินพุธรับข้อมูลก่อนว่า2)ลูปreadเป็นคำๆทีละคำ3)แล้วก็ทำการสลับตามแบบที่ตั้งค่าไว้?ไงวะใช้True falseเป็นลูกบอล แล้วสลับอะ
def A_pattern(position) :
    if position == 1:
        position=2
    elif position== 2:
        position=1
    return position

def B_pattern(position):
    if position == 2:
        position=3
    elif position == 3:
        position=2
    return position

def C_pattern(position):
    if position == 1:
        position=3
    elif position == 3:
        position=1
    return position

        

position = 1
switch_drinking_glasses=str(input("type switch pattern:"))
#พี่เค้าใบ้คือไม่ต้องมีdictใช้แค่ตัวแปรตัวเดียวเก็บว่าตอนนี้มันไปอยู่ที่ไหนแล้ว เช่นตอนนี้สลับก็อยู่ที่1 
for i in range(len(switch_drinking_glasses)):
    if switch_drinking_glasses[i] == "A":
        position=A_pattern(position)#ก็ที่พลาดก็คือเราต้องแทนpositionตัวเดิม
    elif switch_drinking_glasses[i] == "B":
        position=B_pattern(position)
    elif switch_drinking_glasses[i] == "C":
        position=C_pattern(position)
        
print(position)

        
