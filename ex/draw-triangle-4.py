"""
input n and then draw a triangle

n = 5

*********
 *******
  *****
   ***
    *

 1)   
*****
 ****
  ***
   **
    *   
2)
****
***
**
*

"""
n = int(input("enter n:")) 

for i in range(n): # row (แนวนอน) # i=1,2,3,4
    for k in range(i): # column " "
        print(" ", end="")
    for j in range(n-i): # column "*"
        print("*", end="")
    for p in range(n-i-1): # column (แนวตั้ง)
        print("*",end="")
    print()