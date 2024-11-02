"""
1-2 = free
3-5 = 20 / hr.
6-8 = 50 / hr.
9-12 = 80/ hr.
>= 13 = 500

Enter parking hour:

parking fee = ?
"""
parking_hour=eval(input("parking hour:"))
parking_fee_value=0
if parking_hour<0:
    print("ERROR TRY AGAIN")
elif parking_hour<=2:
    print("FREE")
elif parking_hour<=5:
    parking_fee_value=(parking_hour-2)*20
    print(f"parkingfee:{parking_fee_value}")
elif parking_hour<=8:
    parking_fee_value=((parking_hour-5)*50)+60
    print(f"parkingfee:{parking_fee_value}")
elif parking_hour<=12:
    parking_fee_value=((parking_hour-8)*80)+60+150
    print(f"parkingfee:{parking_fee_value}")
elif parking_hour>=13:
    parking_fee_value=500
    print(f"parkingfee:{parking_fee_value}")













