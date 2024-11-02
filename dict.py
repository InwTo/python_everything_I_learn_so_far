person = [30, "Aungkoon", "Kongpet", "Koon", "Male"]
person_dict = {"firstname":"Aungkoon", "lastname":"Kongpet", "nickname":"Koon", "gender":"Male", "age":30} # key:value
#ความแตกต่างของทั้ง2คือdictมีkeyเรียกใช้งานได้เลยต่างจากlistที่ต้องใช้indexเรียก(ยาก) และ แบ่งเป็นหมวดที่ต่างกันได้เช่น ชื่อ อายุ เพศ แต่listต้องเป็นหมวดเดียวกันเช่นคะแนน
print(person[0])
print(person_dict["age"])

person_dict["tel"] = 1234567890 # add new data
print(person_dict)

person_dict["age"] = 28 # edit data by key
print(person_dict)

person_dict.pop("nickname")
print(person_dict)

for key in person_dict: # for-each
    print(person_dict[key])
