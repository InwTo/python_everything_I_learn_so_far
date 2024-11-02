"""
    input phone number: 0811332555

    0 = ?
    1 = ?
    2 = ?
    3 = ?
    4 = ?
    5 = ?
    6 = ?                                                                        
    7 = ?
    8 = ?
    9 = ?
"""
phone_number =input("phonenumber:") # 097654321
phone_value = {"0":0, "1":0, "2":0 ,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0}
for i in range (len(phone_number)):
    phone_value[phone_number[i]]=phone_value[phone_number[i]]+1

for key in (phone_value):
    print(f"{key} = {phone_value[key]}")

max_count=0
max_value=0
for key in  (phone_value):
    if phone_value[key] > max_count:
         max_count = phone_value[key]
         max_value = key

print(f"mode={max_value}({max_count})")








    
    