"""
    เขียนโปรแกรม รับ string มา 1 ประโยคจากนั้นให้มันการนับแยกประเภทว่าประโยคดังกล่าวมี
    - ตัวอักษรพิมพ์ใหญ่กี่ตัว
    - ตัวอักษรพิมพ์เล็กกี่ตัว
    - ตัวเลขกี่ตัว
    - space กี่ตัว

    และพิมพ์ออกทางหน้าจอ

    enter text: I am 30 year olds
"""
sentense=input("type anything:")
all={"upper_text":0,"lower_text":0,"upper_text":0,"number":0,"space":0,"others":0}
for i in range (len(sentense)):
    if (sentense[i]).isupper():
        all["upper_text"]=all["upper_text"]+1
    elif(sentense[i]).islower():
        all["lower_text"]=all["lower_text"]+1 
    elif(sentense[i]).isdigit():
        all["number"]=all["number"]+1
    elif(sentense[i]).isspace():
        all["space"]=all["space"]+1
    else:
        all["others"]=all["space"]+1

for key in all:
    print(f"{key} = {all[key]}")
