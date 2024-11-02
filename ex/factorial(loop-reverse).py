"""
5! = 5*4*3*2*1
Enter number: 8

8! = ....

"""

fact = 1
number = int(input("numberfor!"))
if number == 0 :
    print(1)
elif number < 0 :
    print("error")
else:
    for i in range (number, 0, -1):
        fact = fact*i
    print(fact)





