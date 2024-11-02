import json
file = open("resource/student-data.json", "r")

student_list = json.load(file)
student_list.append({"firstname": "Tony", "lastname": "Ja", "age": "45", "gender": "male"})#เพิ่มdictเข้าไปในlistอีกแต่มันเพิ่มในตัวแปรไม่ใช่file.json
print(student_list)
file.close()


w_file = open("resource/student-data.json", "w")
json.dump(student_list, w_file, indent=4)#dumpคือการถ่ายโอนข้อมูล มันจะส่งข้อมูลคืนไปให้และแปลงให้เป็น.json (student_list)-->ตัวที่จะส่ง (w_file)-->ไฟล์ไหนและแบบไหน (indent=4)-->ย่อหน้ากี่
w_file.close()

