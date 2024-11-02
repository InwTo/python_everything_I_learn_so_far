"""

Welcome to manage ranong restaurant...!!
1. Print all restaurant
2. Add new restaurant
3. Edit restaurant
4. Delete restaurant

Please select your option: 2

ID:2
- restaurant name: KAMU
- Type: Milk tea
- Location: https://
-----------------------
ID:3
- restaurant name: KAMU
- Type: Milk tea
- Location: https://

"""
import requests

def new_info():
    new_data = {#ใส่กรอบตามapiที่เค้ากำหนดมา
        "sheet1": {
            "nameOfRestaurant": "",
            "typesOfFoods": "",
            "levelOfDeliciousness": "",
            "everythingIsDelicious?": "",
            "location": "",
            "recommendedMenu": "",
        }
    }

    name_Of_Restaurant=input("Name Of Restaurant: ")
    typesOfFoods=input("Types of Foods: ")
    levelOfDeliciousness=input("Level of deliciousness(very good/good/so so/bad/very bad): ")
    everythingIsDelicious=input("Every thing is delicious?(yes/no): ")
    location=input("location(please add google map): ")
    recommendedMenu=input("Recommended Menu:")
    new_data["sheet1"]["nameOfRestaurant"]=name_Of_Restaurant
    new_data["sheet1"]["typesOfFoods"]=typesOfFoods
    new_data["sheet1"]["levelOfDeliciousness"]=levelOfDeliciousness
    new_data["sheet1"]["everythingIsDelicious?"]=everythingIsDelicious
    new_data["sheet1"]["location"]=location
    new_data["sheet1"]["recommendedMenu"]=recommendedMenu

   
def check_exist_restaurant(input_new):#1)ส่งค่าที่inputเข้าไป 2)ดึงgetมา 3)เอาชื่อกับโลเคชั่น 4)ถ้าซ้ำ=true ไม่ซ้ำ=false    falseก็addได้
    api_exist_info = requests.get("https://api.sheety.co/140d953326155d618b45dd03014de2e9/dataOfRanongRestaurant/sheet1")
    exist_json = api_exist_info.json()
    list_exist = exist_json['sheet1']
    exist_or_not = False
    for i in range (len(list_exist)):
        if input_new["sheet1"]["nameOfRestaurant"] == list_exist[i]["nameOfRestaurant"]:
            if input_new["sheet1"]["location"] == list_exist[i]["location"]:
                exist_or_not = True
                break
    return exist_or_not
    



def print_all():
    api_retrieve = requests.get("https://api.sheety.co/140d953326155d618b45dd03014de2e9/dataOfRanongRestaurant/sheet1")

    api_json = api_retrieve.json()
    data_list = api_json['sheet1']#ดึงมาเป็นlistก่อนแบบเป็นก้อนเดียว ทำเรื่องยากให้เป็นเรื่อง่ายดิบีม อย่าคิดเยอะ
    max_id = 0
    #เดี่ยวนะถ้า
    if len(data_list) == 0 :
        print("don't have information yet")
    else:
        print("All restaurant")
        for i in range (len(data_list)):
            print(f"ID:{data_list[i]['id']}")
            print(f"- restaurant name:{data_list[i]['nameOfRestaurant']}")
            print(f"- Type:{data_list[i]['typesOfFoods']}")
            print(f"- level of yummy:{data_list[i]['levelOfDeliciousness']}")
            print(f"- Location:{data_list[i]['location']}")
            print(f"- recommend menu:{data_list[i]['recommendedMenu']}")
            print("---------------------------------")
            max_id = data_list[i]['id']
    return max_id

def add_new():
    new_data = new_info()
    exist_or_not = check_exist_restaurant(new_data)
    if exist_or_not == False:
        resp = requests.post("https://api.sheety.co/140d953326155d618b45dd03014de2e9/dataOfRanongRestaurant/sheet1", json=new_data)
        resp_data = resp.json() # {"error"}
    elif exist_or_not == True:
         print("Add fail because already have one!!!!")
    
    if "errors" in resp_data.keys(): # ["error"]
        print("error try again!!")
    else:
        print("successful for adding")

def delete_old():#โอเค กำหนดก่อนมีไรต้องทำบ้าง1)แสดงตัวเลือกทั้งหมด 2)กำหนดให้เค้าไม่ใส่เลขนอกเหนือจากid 3)ลบโดยใช้เลขid
    max_id = print_all() # 6
    Id_delete=int(input("select Id to delete:"))
    if Id_delete < 2 or Id_delete > max_id :
        print("please try again")
    else:
        resp = requests.delete(f"https://api.sheety.co/140d953326155d618b45dd03014de2e9/dataOfRanongRestaurant/sheet1/{Id_delete}")
        resp_data=resp.json()

def edit_new():#1)ขึ้นทั้งหมดให้เลือกทั้งหมด 2)เลือกIdที่จะแก้
    max_id = print_all()
    Id_edit = int(input("select Id to edit"))
    if Id_edit < 2 or Id_edit > max_id :
        print("please try again")
    else:
        new_edit = new_info()
        exist_or_not = check_exist_restaurant(new_edit)
        if exist_or_not == False:
            resp = requests.put(f"https://api.sheety.co/140d953326155d618b45dd03014de2e9/dataOfRanongRestaurant/sheet1/{Id_edit}", json=new_edit)
            resp_data = resp.json()
            print("edit success!!")
        if exist_or_not == True:
            print("Edit fail because already have one!!!!")
                


print("Welcome to manage ranong restaurant...!!")
while True:
    print("1. Print all restaurant")
    print("2. Add new restaurant")
    print("3. Edit restaurant")
    print("4. Delete restaurant")
    print("5. Exit")
    option = int(input("Please select your option: "))
    print()
    if option == 1:
        print_all()
    elif option == 2:
        add_new()
    elif option == 3:
        edit_new()
    elif option == 4:
        delete_old()
    elif option == 5:
        break
    else:
        print("dont have that number!!!!")
    print()
   
   



   
   
   
