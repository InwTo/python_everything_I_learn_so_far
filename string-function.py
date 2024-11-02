#phone = input("Enter phone: ") # "081"
txt = "This is a cat"
phone = "07876364"
phone2 = "086-7865-3556"
#print(phone[0])
for i in range(len(txt)):
    print(txt[i])

print(len(txt))#มันนับแบบเหมือนคนเลย 1234 แต่ ถ้าพวกindexแบบตำแหน่งมันจะนับ 0 1 2 3
print(txt[0])
if txt.islower() : # isascii(), isupper(), islower(), isdigit(), isspace()
    print("True")
    
else:
    print("False")
    

upper_txt = txt.upper()
lower_txt = txt.lower()

print(upper_txt)
print(lower_txt)

txt_list = txt.split(" ") # 14/09/2024 => ["14", "09", "2024"]
print(txt_list)

phone2_list = phone2.split("-")
print(phone2_list)

replace_txt = txt.replace(" a ", "")
print(replace_txt)

greeting = "hello world"
print(greeting)
print(greeting[0:4]) # [start:stop-1] เอาไว้ลบstringได้แต่ต้องเขียนดีๆนะ 
#คือถ้านับhello ได้5ตัวจะเอาแค่hell ต้องเขียน0:5-1 แล้วเดียวมันจะstopลบ1อีกที เป็น 0 1 2 3 อะเค

