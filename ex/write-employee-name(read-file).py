"""
    เขียนโปรแกรม กรอกข้อมูลชื่อพนักงานไปเรื่อยๆ จนกว่าผู้ใช้ จะกรอกตัวเลขเข้ามา
    จากนั้น ให้นำชื่อของ พนักงานทั้งหมด เขียนลง file ชื่อ employee-data.txt โดยจะไม่มีการเก็บชื่อซ้ำ
"""
#infinityloop inputก่อน ถ้าเป็นdigit.ให้break ไม่ก็ใส่เพิ่ม แล้วก็แยกโดนถ้ามีคำซ้ำในlistให้ลบทิ้ง แล้วค่อยไปใส่เพิ่มในfile

employee_name=[]
while 1==1:
    employee=input("give me your employee name:")
    if employee.isdigit():
        break
    else:
        if employee not in employee_name:
            employee_name.append(employee)
             

print(employee_name)

file=open("resource/employee-data.txt","w")
for i in range (len(employee_name)):
        file.write(employee_name[i])
        file.write("\n")



file.close()
#สิ่งที่ได้รู้1)กดctrl+c ออกโปรแกรมให้ถูกไม่งั้นมันจะขึ้นอะไรแปลกๆ 2)ไม่รู้อะไรว่าผิดปกติตรงไหนก็ลองแม่งเลย ลองไปจะเสียหายอะไร แค่มองมันไม่รู้