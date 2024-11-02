"""
Enter number of case: 4000#ก็คือใส่ค่าแล้วก็หาเคสที่เกิน4000แล้วก็print 
""" #1)input2)หาเคสที่ผู้ป่วยเกินเลขที่ใส่มา




#เอางี้ต้องทำไรนะ1)ต้องinputจำนวนเลขที่เกินข้อมูลของเคส2)เปิดไฟล์3)new_case?[key]



#ผลลัพท์ที่อยากได้คือแบบ (week:15) (year:2022) (newcase:4150) how 1)ลูปหาเคสที่เยอะก่อน2)เอาข้อมูลไปเก็บในดิกพร้อมกับสัปดาห์และปีเป็นkey
def find_above_number():
    import requests
    resp = requests.get("https://covid19.ddc.moph.go.th/api/Cases/timeline-cases-all")
    json_data=(resp.json())
    above_number={}
    input_number=int(input("enter your new_case number:"))
    for i in range (len(json_data)):
        if json_data[i]["new_case"]>input_number:
            above_number=(f"(week:{json_data[i]['weeknum']}) (year:{json_data[i]['year']}) (newcase:{json_data[i]['new_case']})")
            print(above_number)

find_above_number()