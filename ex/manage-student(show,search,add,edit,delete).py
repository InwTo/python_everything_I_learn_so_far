import json

#อัน1ทำไง 1)เปิดไฟล์   
"""
    List of all student
    1. Aungkoon Kongpet (tel: 123456789) (Year 2)
    2. Aungkoon Kongpet (tel: 123456789) (Year 2)
"""
#1)เรารับออกมาเป็นlist2)ออกมาสวยๆงี้อยู่ในเรื่องลิสไม่ก็ดิค3)iforตัวเลขด้านหน้า

def show_all_student():
    student_file=open("resource/student-info.json","r")
    student_info=json.load(student_file)
    print("List of all student")
    for i in range (len(student_info)):#2ปัญหา1)dictไม่อ่าน2)ทำให้มันนับเลข1-10ใช้เรื่องloop
        print(f"{i+1}. {student_info[i]['firstname']} {student_info[i]['lastname']} (tel: {student_info[i]['telephone']})  (Year {student_info[i]['year']})")
       # print(f"{i} {student_info[i]['firstname']} )"
    student_file.close()



def search_student():#1)ต้องอินพุทข้อมูลนักเรียนที่จะหาด้วย2)หาด้วยชื่อจริงก่อนโดย3)printออกมาหมดของคนนั้น
    student_name=str(input("Enter student name for search: "))
    student_file=open("resource/student-info.json","r")
    student_info=json.load(student_file) 
    found_or_not=False
    found_student = {}
    for i in range (len(student_info)):
        if student_info[i]['firstname']==student_name :
            found_or_not=True
            found_student = student_info[i]
            break
        else :
            found_or_not=False
    
    
    if found_or_not == True:
        print("Found student....!!!")
        print(f"{found_student['firstname']} {found_student['lastname']} (tel: {found_student['telephone']})  (Year {found_student['year']})")
    elif found_or_not == False:
        print("Not found")
    student_file.close()




def collect_student_info():
    all_student=[]
    student_file=open("resource/student-info.json","r")
    all_student=json.load(student_file)

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
    student_file.close()
    return all_student
        


def dump_file(all_student):
    student_file=open("resource/student-info.json","w")
    json.dump(all_student,student_file,indent=4)



def delete_file():#1)ขึ้นชื่อทุกคนมาก่อน เลือกเหยื่อที่จะลบ<--ใช้อันเดิมดิฟังชั่น2)พิมเลขที่จะลบ i แน่นอน 3)ลบจากlist
    student_file=open("resource/student-info.json","r")
    student_info=json.load(student_file) 
    student_file.close()
    while True:
        number_student=int(input("Enter number student for delete: "))
        found_or_not=False
        for i in range (len(student_info)):
            if i+1==number_student :
                found_or_not=True
                student_info.remove(student_info[i])
                break
            else:
                found_or_not=False
        
        if found_or_not==True:
            print("Delete success...!!")
            break
        else:
            print("Student number invalid, please try again...!!!")
    return student_info
    
       
def edit_file():#1)ขึ้นชื่อทุกคนมาก่อน2)ขึ้นพิมมาบอกว่าให้select number3)ขึ้นมาให้ใส่ข้อมูลใหม่4)เอาข้อมูลใหม่แทนลำดับข้อมูลที่ถูกเลือก5)dump file
    student_file=open("resource/student-info.json","r")
    student_info=json.load(student_file) #เพื่อประสิทธิภาพแบบว่าเว็ปโหลดเร็วเราควรเอาไฟล์มาข้างนอกจะได้ไม่ต้องโหลดหลายรอบ และปิดไฟล์ด้วย
    student_file.close()
    found_or_not=False
    while True:
        number_student=int(input("select number for edit: "))
        for i in range (len(student_info)):
            if i+1==number_student :
                print("enter new infomation for student") 
                found_or_not=True
                new_info_student={"firstname":0,"lastname":0,"telephone":0,"year":0}
                new_info_student["firstname"]=input("enter firstname: ")
                new_info_student["lastname"]=input("enter lastname: ")
                new_info_student["telephone"]=int(input("enter telephone: "))
                new_info_student["year"]=int(input("enter year: "))
                student_info[i]=new_info_student
                break
            else:
                found_or_not=False
                
        if found_or_not==True:
            print("Edit success...!!")
            break
        else:
            print("Student number invalid, please try again...!!!")
    return student_info
       






print("Welcome to Student management system.....!!")


#1)infinity loop 2)if-else เลือกตัวเลข 3)ข้อ6exit 4)เราใช้แต่ข้อเป็นฟังชั่นแล้วเรียกใช้ในแต่ละifelseได้นี้หว่า5)อ่านไฟล์เขียนไฟล์เราเอาให้ครบจบในที่เดียวเลยดีกว่า

while True:
    print("Please select your choice")
    print("1. Show all student")
    print("2. Search student")
    print("3. Add new student")
    print("4. Edit student")
    print("5. Delete student")
    print("6. Exit")

    choice = int(input("Enter choice number: "))
    if choice == 1:
        show_all_student()
    elif choice == 2:
        search_student()
    elif choice == 3:
        student_info=collect_student_info()
        print(student_info)
        dump_file(student_info)
    elif choice == 4:
        show_all_student()
        new_list=edit_file()
        dump_file(new_list)
    elif choice == 5:
        show_all_student()
        new_list=delete_file()
        dump_file(new_list)

    elif choice == 6:
        break
    print(".")
    print(".")
    print(".")











