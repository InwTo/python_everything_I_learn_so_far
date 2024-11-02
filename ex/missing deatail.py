##input loop list If else เราต้องรับinputเป็นstingก่อนแล้วก็loop string 1)คือเราinputมาก่อน 2)ทำระบบเช็คแต่ละตัว 3)แล้วเอาแต่ละตัวนั้นมาเช็คกับเลขที่มี 4)มาลบหรอแบบถ้าไม่เหลือก็พิมNo missing detail 
data = str(input("type number: ")) # 11100456
number=["1","2","3","4","5","6","7","8","9","0"]
for i in range(len(data)):#แล้วถ้าเลขซ้ำๆแบบ0000จะต้องทำไงวะ
    if data[i] in number:
        number.remove(data[i])


if len(number) == 0:
    print("No missing digits")
else:
    for i in range(len(number)):
        print (number[i], end=" ")
#outputให้เป็นเลข สวยๆ  0 9 1

#ตอนนี้ผิด2ตรงคือมันลบเกิน-->เราใช้คำสั่งผิดแน่เลย และก็เปลี่ยนstr to intไม่ได้
#ปัญหาคือทำไมมันถึงnomissingdetailก่อนเลย