"""
    เขียนโปรแกรม รับเลขค่าอาหารที่รับประทาน จากนั้นนำ คำนวณหา VAT และ service charge และรวมเลขทั้งหมด พิมพ์ออกมาเป็น Grand total 
"""
food_price = eval(input("food price:"))
vat = (food_price*0.07)
foodandvat = (food_price+vat)
service_charge =(foodandvat*0.1)
Grand_totol = (foodandvat+service_charge)

print(f"vat : {vat:.2f}")
print(f"service_charge : {service_charge:.2f}")
print(f"Grand_totol : {Grand_totol:.2f}")