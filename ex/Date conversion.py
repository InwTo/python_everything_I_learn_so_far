#แปลงจาก08/27/2024 เป็น 27 aug 2014 ใช้ Dict input loopปะวะ str fuction
date = input("mm/dd/yyyy:") 
date_list = date.split("/")#split
#print(date_list) #["12", "11", "2024"]
date_dict = {"1":"Jan","2":"Feb","3":"Mar","4":"Apr","5":"May","6":"Jun","7":"Jul","8":"Aug","9":"Sep","10":"Oct","11":"Nov","12":"Dec"}

print(f"{date_list[1]} {date_dict[date_list[0]]} {date_list[2]}")


