
"""
    Welcome to covid 19 data history!!!
    1. Search for new case
    2. Search for new death
    3. Search for new recovery
    4. Search for case foreign
    Key chioce for searching: 1

    Enter new case number: 

"""


import requests
resp = requests.get("https://covid19.ddc.moph.go.th/api/Cases/timeline-cases-all")
json_data=(resp.json())

def find_new_case(case_list): # [2,4] รับค่ามาเป็นลิสแล้วก็หาลูปได้เลย นี้เป็นครั้งแรกที่รับค่าเป็นลิสในฟังชั่น
    all_choice={"new case":0,"new death":0,"new recovery":0,"case foreign":0,}
    for i in range(len(case_list)):
        if case_list[i] == 1:
            input_number=int(input("enter your new case number:"))
            all_choice["new case"]=input_number
        elif case_list[i] == 2:
            input_number=int(input("enter your new death number:"))
            all_choice["new death"]=input_number
        elif case_list[i] == 3:
            input_number=int(input("enter your new recovery number:"))
            all_choice["new recovery"]=input_number
        elif case_list[i] == 4:
            input_number=int(input("enter your new case number:"))
            all_choice["case foreign"]=input_number 

           
            
    for i in range (len(json_data)):
        if json_data[i]["new_case"]>=all_choice["new case"] and json_data[i]["new_death"]>=all_choice["new death"] and json_data[i]["new_recovered"]>=all_choice["new recovery"] and json_data[i]["case_foreign"]>=all_choice["case foreign"]  :
            above_number=(f"(week:{json_data[i]['weeknum']}) (year:{json_data[i]['year']}) (newcase:{json_data[i]['new_case']}) (new death:{json_data[i]['new_death']}) (new recovered:{json_data[i]['new_recovered']}) (case_foreign:{json_data[i]['case_foreign']})")            
            print(above_number)

print("Welcome to covid 19 data history!!!")
while True :
    print("1. Search for new case")
    print("2. Search for new death")
    print("3. Search for new recovery")
    print("4. Search for case foreign")#ทำไงให้รับได้หลายตัวและยังสามารถกรองจากตรงนั้นได้1)inputต้องเก็บเป็นdictแบบตั้งชื่อเลยว่าall choice={new_death:3000,new_case:4000,new_fo:0,new_re:100}2)ทำandในifให้หมดโดยใช้keyเรียกมาแบบข้างนif json_data[i]["case_foreign"]>=all_choice["newdeath"]and json_data[i]["new_recovered"]>=all_choice["newdeath"]
    print("5. exit")
    input_choice=input("Key chioce for searching: ")#ทำให้มันสามารถรับแบบ1,2แล้วทำงาน2อันได้
    break_or_not=False
    input_choice2=input_choice.split(",")
    for i in range (len(input_choice2)):
        input_choice2[i]=int(input_choice2[i])


    if 5 in input_choice2: #ใช้แบบนี้ได้ด้วย เอามาใช้ว่ามีตัวนั้นมั้ยถ้ามีก็ breakแม่งเลย
        print("exit success...!!!")
        break
    for i in range (len(input_choice2)): # [1,2,3,4,8]
        if input_choice2[i] > 4 or input_choice2[i] < 1 :
            break_or_not=True   
            break
    if break_or_not==False:
       find_new_case(input_choice2)     
    elif break_or_not==True:   
        print("you enter wronf number...!!!")
        continue
       
    
 
    




