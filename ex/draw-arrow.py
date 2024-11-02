"""
input n and then draw a arrow

n = 5 // 2 = 2

    *
   ***
  *****
   |||
   |||
  n=6 
    *
   ***
  *****
   |||
   |||
   |||
n = 7
    *
   *** 
  *****
 *******
  |||||
  |||||
  |||||


1)
    *
   ***
  *****
2)
   |||
   |||
"""
n = int(input("enter n:")) 
m=n//2
t=n-m
for i in range(t): # row (แนวนอน) # i=1,2,3,4
    for k in range(n-i-1): # column " "
        print(" ", end="")
    for j in range(i+1): # column "*"
        print("*", end="")
    for p in range(i): # column (แนวตั้ง)
        print("*",end="")
    print()
for i in range(m): # row (แนวนอน) # i=1,2,3,4
    for k in range(m+1): # column " "
        print(" ", end="")
    for j in range(m): # column "*"
        print("|", end="")
    for p in range(m-1): # column (แนวตั้ง)
        print("|",end="")
    print()