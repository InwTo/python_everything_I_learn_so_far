order_of_people=int(input("order preple:"))
file=open("resource/data.txt","r")

index=0
found_or_not=False
#line_no_enter=line.replace("/n","")
#spritก่อน จากนั้นเช็คว่าข้างหน้าเป็นnameมั้ยถ้าเป็น+1 แล้วก็เช็คว่าorder_of_people =indexมั้ยถ้าเท่าก็พิมแสดงออกและfound0rnot=trueเลยถ้าไม่ก็ไปต่อเจอไม่เจอก็ทำifelseแบบเดิม
for line in file:
    line_split=line.split(":")
    #print(line_split)
    if line_split[0]=="Name":
        index=index+1
        if order_of_people==index:
            found_or_not=True
            people_name=line_split[1].replace("\n","")
            len_people_name=len(people_name)
            print(f"{people_name[1:len_people_name]}")
            break

if found_or_not==False:
   print("Not found")

file.close()

