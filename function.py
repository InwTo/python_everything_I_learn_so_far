def cal_sum():
    sum = 0
    # sum = 1+2+3+4+....+10
    for i in range(1, 11):
        sum = sum + i
    print(sum)

def cal_factorial(): # define function เอาไว้เก็บกระบวนการหรืออะไรก็ได้เราต้องการเหมือนเก็บไว้ในคีย์ลัด มีไว้เพื่อแบ่งส่วนโค้ดพร้อมชื่อและสามารถเอาโค้ดที่ใส่ข้างในมาใช้ซ้ำได้
    fact = 1
    for i in range(1, 6):
        fact = fact * i
    print(fact)

def x_plus_y(x, y) -> int#returnเป็นint: # parameters (x, y)เป็นตัวรับค่าและส่งค่าไปให้ฟังช์ชั่น และรับค่าตามตำแหน่ง เช่น x_plus_y(45, 70) --> x=45 y=70
    result = x+y
    return result # 115 มันจะส่งค่าคืนไปให้บรรทัดที่มันcall functionในนี้115ก็returnส่งไปนอกฟักชั่นให้ x_plus_y(45, 70) แต่ต้องมี ตัวรับค่าด้วย(ไม่งั้นจะหายไปกับอากาศ) เป็นแบบนี้  result1 = x_plus_y(45, 70) ก็จะดึงresultมาใช้ได้เลยจากข้างนอก print(f"result1 in main {result1}") ก็จะได้115 
#return หน้าที่คือ ไว้ส่งค่าคืนไปmain program ทำให้ดึงค่า เช่น115 มาใช้ต่อข้างนอกฟังชั่นได้


# main program เป็นโปรแกรมนอกฟังชั่น
cal_factorial() # call function เรียกใช้งานฟังช์ชันทำให้โค้ดข้างในมันทำงาน
cal_factorial()
result1 = x_plus_y(45, 70) # send argument อันนี้เป็นตัวส่งค่าแบบที่ยกตัวอย่าง x_plus_y(45, 70) --> x=45 y=70 ต้องมีตัวรับด้วยresult1
print(f"result1 in main {result1}")
num1 = int(input("Enter number: "))#อันนี้ตัวอย่างโชว์ว่าสามารถรับค่าinputจากข้างนอกได้
num2 = int(input("Enter number: "))
result2=x_plus_y(num1, num2)
#สรุปอีกที เวลาส่งreturn เช่นresult(115) มีตัวรับค่าด้านอกคือ result2 = x_plus_y(num1, num2) ไอวงเล็บนี้อะคือส่งparameter ก็คือส่งค่าจากด้านนอกไปด้านในฟังก์ชั่น ไม่ใช่return bro okieนะ 