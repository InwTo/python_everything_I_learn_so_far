"""
    เขียนโปรแกรม รับค่าคะแนนสอบของนักเรียนไปเรื่อยๆ หยุดเมื่อกรอก -1 (เก็บใส่ list)
    จากนั้น ให้นำคะแนนสอบทั้งหมด มาหาค่า

    - ผลรวม
    - ค่าเฉลี่ย
    - ค่าต่ำสุด
    - ค่าสูงสุด
    - ค่ามัธยฐาน
    ฐานนิยม
"""
student_score = []

while True:
    data_input=eval(input("Enter your student score:(-1 to exit)"))
    if data_input<-1 or data_input > 100:
        print("try again")
    elif data_input == -1:
        break
    else:
        student_score.append(data_input)

student_score.sort()
max_value = max(student_score)#สูงสุดในลิส
min_value = min(student_score)#ต่ำสุดในลิส
sum_value = sum(student_score)#ผลรวมในลิส
average_value = sum_value/(len(student_score))
mid_position = len(student_score)//2
Number_student_score= len(student_score)
if len(student_score) % 2 == 1 :
    median_value = student_score[mid_position]
    
else:
   median_value = (student_score[mid_position]+student_score[mid_position+1])/2




print(f"max={max_value:.2f}")
print(f"min={min_value:.2f}")
print(f"sum={sum_value:.2f}")
print(f"median={median_value:.2f}")
print(f"average={average_value:.2f}")
print(student_score)


max_count = 0
max_value = student_score[0]
for i in range (Number_student_score):
    count_score = student_score.count(student_score[i])
    if count_score > max_count:
        max_count = count_score
        max_value = student_score[i]


if max_count < 2:
    print("don't have mode")
else:
    print(f"mode = {max_value} ({max_count})")

