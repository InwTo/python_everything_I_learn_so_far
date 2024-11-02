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
    for j in range(i+1): # column (แนวตั้ง)
        print("*",end="")
    print()

#เอาไงดีวะ 



