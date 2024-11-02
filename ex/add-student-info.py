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

def input_one_student():
    student = {"firstname":0,"lastname":0,"telephone":0,"year":0}
    student["firstname"]=input("enter firstname: ")
    student["lastname"]=input("enter lastname: ")
    student["telephone"]=int(input("enter telephone: "))
    student["year"]=int(input("enter year: "))
    print(student["firstname"])
    all_student.append(student)
    return all_student





"""def y_n_infinity(x):
    while 1==1:
        x
        y_n=input("do you want to continue(Y/N):")
        if y_n=="Y":
            continue

        elif y_n=="N":
            break"""

        
def dump_file(all_student):
    student_file=open("resource/student-info.json","w")
    json.dump(all_student,student_file,indent=4)




all_student=[]#งงนิดนึงไมมันอ่านค่านี้ในฟังชั่นได้วะ เข้าใจตรงเก็บที่มันเก็บข้างนอกฟังชั่นทำให้ลูปแล้วเก็บตัวเก่าได้ อ๋อหรือมันแค่กำหนดให้all_studentรับค่าเป็นdictเฉยๆวะ
while 1==1:
        all_student=input_one_student()
        print(all_student)
        y_n=input("do you want to continue(Y/N):")
        if y_n=="Y":
            continue

        elif y_n=="N":
            break

dump_file(all_student)