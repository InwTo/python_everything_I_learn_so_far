"""
    เขียนโปรแกรม รับค่า ตัวเลข newcase ที่ต้องการค้นหา จากนั้น
    ให้ทำการค้นหา ใน api ของ covid ว่า มีสัปดาห์ไหนบ้าง ที่มีผู้ติดเชื้อเกินจำนวน input ที่กรอกเข้ามา

    1500

    List of week (> 1500) 
    - Week 2 Year 2022
    - Week 3 Year 2022
"""
#1)ลูปเพื่อดึงnewcaseในแต่ละlist เสร็จและ2)ภ้าi newcase>699 ให้add i weeknumมาใส่ในlistใหม่?

import requests

resp = requests.get("https://covid19.ddc.moph.go.th/api/Cases/timeline-cases-all")
#print(resp.json())
data = resp.json()

num_newcase=int(input("newcase over :"))
num = []
for i in range(len(data)):
    if data[i]["new_case"] > num_newcase :
        print(f"week:{data[i]['weeknum']} year{data[i]['year']}")
        num.append(data[i]['weeknum'])

print(f"count week (> {num_newcase}) = {len(num)}")    
