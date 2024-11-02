


# i is int variable
"""for i in range(10): # (stop-1) 0-9
    print(i)"""

"""for i in range(5, 18): # (start, stop-1) 5-17
    print(i)"""

"""for i in range(1, 19, 3): # (start, stop-1, step) 1-18 => 1, 4, 7, 10, 13, 16
    print(i)"""

"""for i in range(10, 0, -1): # (start, stop-1, step)
    print(i)"""

"""j = 0
while j<10:
    print(j)
    j = j+1
"""

# 1+2+3+4+5+6+7+8+9+10
sum = 0    
for i in range(1, 11, 1):
    sum = sum+i
print(sum)

"""
    Round 1
    - i=1
    - sum = 0+1 = 1

    Round 2
    - i=2
    - sum = 1+2 = 3

    Round 3
    - i=3
    - sum = 3+3 = 6

"""
for j in range(2):
    for i in range(5,19):
        print(i)