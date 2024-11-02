"""
    เขียนโปรแกรม รับเลขค่าอาหารที่รับประทาน จากนั้นนำ คำนวณหา VAT และ service charge และรวมเลขทั้งหมด พิมพ์ออกมาเป็น Grand total 
"""
food_price = eval(input("food price:"))
vat_value = 0
service_charge_value=0
while 1==1:
    vat=input("Vat Y/N")
    if vat == "Y":
        vat_value = (food_price*0.07)
        print(f"vat : {vat_value:.2f}")
        break
    elif vat == "N":
        print("No vat")
    else:
        print("Tryagain")

total = food_price+vat_value
while True:
    service_charge=input("Service_charge Y/N")
    if service_charge == "Y":
        service_charge_value = (total*0.1)
        print(f"servicecharge : {service_charge_value:.2f}")
        break
    elif service_charge == "N":
        print("No service charge")
        break
    else:
        print("Tryagain")

grand_totol = (total+service_charge_value)
print(f"grand_totol :{grand_totol:.2f}")





