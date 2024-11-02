"""
    เขียนโปรแกรม รับค่าชื่อพนักงานเข้ามา จากนั้นให้นำไปค้นหาใน file (name.txt)
    ว่าเจอหรือไม่ ถ้าเจอให้แสดงเป็นลำดับที่เจอ ถ้าไม่เจอให้โชว์ว่า Not found

    Found June at index 5
"""
employee=str(input("press employee name :"))
file=open("resource/name.txt","r")

index=0
found_or_not=False
#False==("notfound")ต้องทำเป็นIF else
#True==("found")
#truefalse
#true=found
#false=notfound
for line in file:
    line_noenter=line.replace("\n", "")
    index=index+1
    if line_noenter==employee:
        found_or_not=True
        break

if found_or_not == True:
    found_or_not2=("Found")
    print(f"{found_or_not2} {employee} at index { index}")
elif found_or_not == False:
    found_or_not2=("Not Found")
    print(f"{found_or_not2}")

file.close()
