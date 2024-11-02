print("Hello")
print("World")

"""
    Data type of variable
    - int (เลขจำนวนเต็ม)
    - float (เลขทศนิยม)
    - string (ตัวหนังสือ ตัวอักษร)
    - boolean (ค่าความจริง) = True, False
    - array/list (เก็บค่าเป็นชุด เป็นกลุ่ม)


    Operator
    1. Number
        - + (3)
        - - (3)
        - * (2)
        - / (2)
        - // (2)
        - % (mod) (2)
        - ** (1)
    2. String
        - +
        - *
    3. boolean
        - and
        - or
        - not
"""

x = 5
y = 2
vat = 0.07
my_name = "Beam"
boo = True

result = x % y
#2x+3y-x^2
result2 = (2*x)+(3*y)-(x**2)
result3 = 10+2-8/4*6 # 10+2-2*6 => 10+2-12 => 12-12 => 0
result4 = (((10+2)-8)*4)/6

# 5 % 2 = 1
print(str(x) +" % "+ str(y) + " = "+str(result)) # result = 1 => "1"
print(f"{x} % {y} = {result}")
print(f"My result2 = {result2}")
print(result3)
print(f"Result4 = {result4:.2f}")

print(my_name+"!!!!"+".......")
print(my_name*4)

print(boo and True) # True
print(boo and False) # False
print(boo or False) # True
print(False or False) # False
print(not boo) # False
False=="woo"
print(False)

#หารเอาเศษ2ไงวะ
#มันต้องเอา.2fมาใช้ด้วย

test ="2+2"
print(int(test))