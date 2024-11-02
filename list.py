"""score1 = 80
score2 = 54
score3 = 65
score4 = 55"""

score_list = [80, 65, 54,  55, 54]

print(score_list) # print all data
print(score_list[0]) # print data by index
print(score_list[0:2]) # print data by range

print(f"length = {len(score_list)}") # count size of list

score_list.append(100) # add new data to the list
print(score_list)
if 99 in score_list:#ไว้ใช้เช็คข้อมูลตัวซ้ำได้ หรือเช็คว่ามีตัวนั้นมั้ย เอามาใช้กับbreak ได้เหมือนกัน และเราสามารถใส่ not เพื่อเช็คว่าถ้าไม่มีตัวนั้นๆในนี้เราจะทำ...อะไรก็ว่าไป เช่น if employee not in employee_name:
   score_list.remove(99) # remove data #ไม่จำเป็นต้องremoveเราจะไปตั้งให้ทำอย่างอื่นก็ได้ เช่น employee_name.append(employee)
print(score_list)

score_list[0] = 99 # edit data by index

for i in range(len(score_list)): # loop over list by index
    print(score_list[i])





max_value = max(score_list)
min_value = min(score_list)
sum_value = sum(score_list)

print(f"min = {min_value}")
print(f"max = {max_value}")
print(f"sum = {sum_value}")

score_list.sort()
print(score_list)

score_list.sort(reverse=True)
print(score_list)

count_score = score_list.count(score_list[5]) 
count_score99 = score_list.count(100) 
print(count_score)
print(count_score99)



