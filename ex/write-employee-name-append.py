

file=open("resource/employee-data.txt","r")
employee_name=[]
for line in file:
    line_noenter=line.replace("\n","")
    employee_name.append(line_noenter)

print (employee_name)#list2อัน อันนึงไว้เก็บจากชื่อที่อ่านจากไฟล์ อีกอันเก็บสิ่งที่input ไม่งั้นก็จะappendเก็บไปด้วย

employee_name2=[]

while 1==1:
    employee=input("give me your employee name:")
    if employee.isdigit():
        break
    else:
        if employee not in employee_name:#เช็คในไฟล์ว่าซ้ำมั้ย
            if employee not in employee_name2:#ต้องเช็คว่าซ้ำกับตัวในlistมั้ย 
                employee_name2.append(employee)
        
print(employee_name)
print(employee_name2)

file2=open("resource/employee-data.txt","a")
for i in range (len(employee_name2)):
        file2.write(employee_name2[i])
        file2.write("\n")

