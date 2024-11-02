"""
input m,n and then draw a square m x n

m = 5
n = 4

****
****
****
****
****
"""

m = int(input("Enter m: ")) # 5
n = int(input("Enter n: ")) # 4

for i in range(m): # rows (แนวตั้ง)มันต้องเป็นแนวนอนดิ
    for j in range(n): # column (แนวนอน?)มันต้องเป็นแนวตั้งดิ
        print("*", end="")#เอาไว้ให้มันอยู่บรรทัดเดียวกัน
    print()#เอาไว้ขึ้นบรรทัดใหม่

