"""
input n and then draw a triangle

n = 5

    *
   **
  ***
 ****
*****

"""

n = int(input("enter n:")) 

for i in range(n): # row (แนวนอน) # i=1,2,3,4
    for k in range(n-i-1): # column " "
        print(" ", end="")
    for j in range(i+1): # column "*"
        print("*", end="")
    print()
#เอาไง ก็เราต้องให้มีที่โล่งหน้ามันก่อน จริงๆมันคืออันเดิมแต่เราต้องใส่ที่ว่างข้างหน้า หรือเราต้องมีลูปอีกตัวหรือยังไง คิดๆ
#มันinvertกันอะ