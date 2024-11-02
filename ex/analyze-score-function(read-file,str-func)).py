def list_nisit(file):#example.txt
        replace_line1=line.replace("/"," ") or line.replace(","," ")
        replace_line2=replace_line1.replace("\n","")
        split_line= replace_line2.split(" ")#ทำให้มันเก็บข้อมูลได้แยกกันทั้ง3บรรทัด
        score_list = split_line[1:6]#ทำให้เป็น{5812322211:60,5812322212:70}
        for i in range (len(score_list)) :     #ทำให้เป็นintทีเดียวไม่ได้ทำได้ทีละครั้ง ดังนั้นลูปวนไปทีละตัว
            score_list[i]=int(score_list[i])
            
        return score_list,split_line    
            



def cal_grade(score_list,split_line):   
    sum_score=sum(score_list)
    if sum_score>100 or sum_score<0:
        print(f"{split_line[0]} error")
    elif sum_score>=80:
        print(f"{split_line[0]} A")
    elif sum_score>=75:
        print(f"{split_line[0]} B+")
    elif sum_score>=70:
        print(f"{split_line[0]} B")
    elif sum_score>=65:
        print(f"{split_line[0]} C+")
    elif sum_score>=60:
        print(f"{split_line[0]} C")
    elif sum_score>=55:
        print(f"{split_line[0]} D+")
    elif sum_score>=50:
        print(f"{split_line[0]} D")
    elif sum_score<50:
        print(f"{split_line[0]} F")




input_file=str(input("give me your nisit scrore file:"))#resource/example.txt
file=open((f"resource/{input_file}"),"r")
for line in file :
    score_list_return,split_line_return=list_nisit(file)
    print(score_list_return)
    cal_grade(score_list_return,split_line_return)

file.close()
 

