"""
    เขียนโปรแกรม รับ/กรอก ข้อมูล นักเรียนเข้ามาเรื่อยๆ จนกว่า user จะสั่งหยุด
    จากนั้นให้นำข้อมูลของนักเรียน ทุกคนที่กรอกเข้ามาได้เก็บลงใน file ชื่อ student-info.json

    ex.
    enter firstname: ...
    enter lastname: ...
    enter tel: ...
    enter year: ...

    do you want to continue(Y/N): n
"""
#มันเก็บข้อมูลเป็นdictก่อนสำหรับรายละเอียดแล้วค่อยเก็บเป็นคนๆโดยlist
#1)inputใส่ใน student = {"firstname":0,"lastname":0,"telephone":0,"year":0}ให้ได้และlist เช็ค
#2)ลูปinfinityถ้าYใส่continueถ้าNใส่break เช็ค
#3)dumpลงไฟล์

import json

#แก้เป็น
def collect_student_info():
    all_student=[]#โหลดไฟล์เก่ามาในดิกรูปarrayก่อนแล้วwriteแม่งเลย
    student_file=open("resource/student-info.json","r")
    student_info=json.load(student_file)
    all_student.append(student_info)
    while True:
        student = {"firstname":0,"lastname":0,"telephone":0,"year":0}
        student["firstname"]=input("enter firstname: ")
        student["lastname"]=input("enter lastname: ")
        student["telephone"]=int(input("enter telephone: "))
        student["year"]=int(input("enter year: "))
        print(student["firstname"])
        all_student.append(student)
        y_n=input("do you want to continue(Y/N):")
        if y_n=="Y":
            continue

        elif y_n=="N":
            break
    return all_student
        


def dump_file(all_student):
    student_file=open("resource/student-info.json","w")
    json.dump(all_student,student_file,indent=4)



student_info=collect_student_info()
print(student_info)
dump_file(student_info)