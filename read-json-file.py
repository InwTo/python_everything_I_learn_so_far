"""[
    {"firstname": "Aungkoon", "lastname": "Kongpet", "age": "31", "gender": "male"},
    {"firstname": "Sawitree", "lastname": "Suekam", "age": "27", "gender": "female"},
    {"firstname": "John", "lastname": "Doe", "age": "22", "gender": "male"},
    {"firstname": "June", "lastname": "Homes", "age": "33", "gender": "female"}
]"""

import json  #json เป็นคำสั่งที่ยังไม่พร้อมใช้งาน ทำให้ต้องขอการใช้ ซึ่งมีอีกมากที่เป็นแบบนี้ แต่ที่พร้อมใช้งานเลยก็มีอย่างprintที่พิมแล้วกดใช้ได้เลย

file = open("resource/student-data.json", "r")
student_list = json.load(file)#แปลงจาก ไฟล์ "ตัวอย่าง.jason" --> list/dict  แล้วก็ต้องมีตัวมารับค่าด้วย student_list = json.load(file)
print(student_list[2]["age"])
file.close()


