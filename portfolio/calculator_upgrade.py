#อันแรกสุดคือimportมา ต่อมาก็สร้างappให้เปิดแล้วโชว์ได้ จากนั้นวางlayout แล้วก็ทำรูปปุ่มก่อน แล้วต่อด้วย
# ทำก่อน
import tkinter as tk #มันlibrary เพื่อใช้ไอหน้าต่างลอยได้อันนี้ เราต้องไปโหลดเพิ่ม แล้วมันต้องใช้2ตัวนี้
import customtkinter as ctk
dot = 0
current_value = "0"
result_now = ""
value_equation=""

def input_number(number_cal:str):#เอางี้เผื่อมึนคือเราส่งค่าที่ฟังชั่นก่อนตอนกด จากนั้นก็เพิ่มตัวหลัง ไอc ค่อยคิด
    global current_value
    global dot
    #ตั้งสติก่อน ตอนนี้เราดึงจากปุ่มมาใส่ฟังชั่นได้แล้วเราก็เอามาต่อแล้วก็โชวฺ์ในlabel
    if current_value == "0" :
        if number_cal == "." :
            current_value = current_value+number_cal
        else:
            current_value = number_cal    
    elif number_cal == ".":#ทำไงวะเช็คก่อนออว่ามันเป็น.มั้ย คำสั่งเช็คคือ
        if number_cal not in current_value:
            current_value = current_value + number_cal
    else:
        current_value = current_value + number_cal
    
    #test print #ปัญหาที่เจอคือเลขมันไม่ต่อ ต้องทำให้มันต่อแล้วก็แสดงผล
    output_number()

def output_number():
    result_label.configure(text=f"{current_value}")

def output_equation():
    Equation.configure(text=f"{value_equation}")


def C_number(C_cal:str):
    global current_value
    global value_equation
    if C_cal == "C":
        current_value = "0"
        value_equation = ""
    output_equation()
    output_number()

def delete_number(delete_cal:str):
    global current_value
    if delete_cal == "<":#เราจะให้มันลบถ้าเป็น0เป็น0เหมือนเดิม พอลบตัวเลข ตัวหลังสุดจะหาย แล้วก็ทศนิยมจะหายถ้าลบไม่ใช่ตัวเลข
        #current_value #นับเลขยังไงวะ แบบว่ามีทั้งหมด5ตัวตัวอักษร lenมะ
        current_value = current_value[0:len(current_value)- 1]
    output_number()
    
#โอเค บีม ใจเย็นๆเราไม่ต้องทำหมดให้เสร็จภายในคราวเดียว คิดที่ละขั้นละตอน แล้วโฟกัสที่ละขั้นละตอนพอ ไม่ต้องคิดเยอะเกินไป
#ตอนนี้ที่ต้องทำคือพิมสมการแล้วให้มันขึ้นในdisplayเล็กก่อน
def equation_display(operator:str):
    global current_value
    global value_equation
    value_equation = current_value + operator
    current_value = "0"
    output_equation()

def plus_number():#เอา
    global current_value
    global value_equation



app = ctk.CTk() #อันนี้คือสร้างหน้าwindowขึ้นมาใหม่
app.geometry("1000x1000") #กำหนดขนาด
app.title("calculator plus")

Equation = ctk.CTkLabel(app, text="", fg_color="transparent" , font=("",20), justify="right")
Equation.pack(pady=(40,0))

result_label  = ctk.CTkLabel(app, text="0", fg_color="transparent" , font=("",60))
result_label.pack()

#ทำไรบ้างนะ ขึ้น2ตัวแล้ว แล้วก็กดตวเลขมาต่อก่อน


frame = ctk.CTkFrame(app,fg_color="transparent")
frame.pack(pady=30)


number_1 = ctk.CTkButton(frame, text="1", fg_color="black", width=100, height=100, font=("",40),command=lambda:input_number("1"))#,command=button_event
number_1.grid(row=0 , column = 0 , padx=5 ,pady=5)
number_2 = ctk.CTkButton(frame, text="2", fg_color="black", width=100, height=100, font=("",40),command=lambda:input_number("2"))
number_2.grid(row=0 , column = 1 , padx=5 ,pady=5)
number_3 = ctk.CTkButton(frame, text="3", fg_color="black", width=100, height=100, font=("",40),command=lambda:input_number("3"))
number_3.grid(row=0 , column = 2 , padx=5 ,pady=5)
number_4 = ctk.CTkButton(frame, text="4", fg_color="black", width=100, height=100, font=("",40),command=lambda:input_number("4"))
number_4.grid(row=1 , column = 0 , padx=5 ,pady=5)
number_5 = ctk.CTkButton(frame, text="5", fg_color="black", width=100, height=100, font=("",40),command=lambda:input_number("5"))
number_5.grid(row=1 , column = 1 , padx=5 ,pady=5)
number_6 = ctk.CTkButton(frame, text="6", fg_color="black", width=100, height=100, font=("",40),command=lambda:input_number("6"))
number_6.grid(row=1, column = 2 , padx=5 ,pady=5)
number_7 = ctk.CTkButton(frame, text="7", fg_color="black", width=100, height=100, font=("",40),command=lambda:input_number("7"))
number_7.grid(row=2 , column = 0 , padx=5 ,pady=5)
number_8 = ctk.CTkButton(frame, text="8", fg_color="black", width=100, height=100, font=("",40),command=lambda:input_number("8"))
number_8.grid(row=2 , column = 1 , padx=5 ,pady=5)
number_9 = ctk.CTkButton(frame, text="9", fg_color="black", width=100, height=100, font=("",40),command=lambda:input_number("9"))
number_9.grid(row=2, column = 2 , padx=5 ,pady=5)
number_0 = ctk.CTkButton(frame, text="0", fg_color="black", width=100, height=100, font=("",40),command=lambda:input_number("0"))
number_0.grid(row=3, column = 1 , padx=5 ,pady=5)
delete_C = ctk.CTkButton(frame, text="C", fg_color="black", width=100, height=100, font=("",40),command=lambda:C_number("C"))
delete_C.grid(row=3, column = 0 , padx=5 ,pady=5)
comma = ctk.CTkButton(frame, text=".", fg_color="black", width=100, height=100, font=("",40),command=lambda:input_number("."))
comma.grid(row=3, column = 2 , padx=5 ,pady=5)
delete = ctk.CTkButton(frame, text="<", fg_color="black", width=100, height=100, font=("",40),command=lambda:delete_number("<"))
delete.grid(row=0, column = 3 , padx=5 ,pady=5)
plus = ctk.CTkButton(frame, text="+", fg_color="black", width=100, height=100, font=("",40),command=lambda:equation_display("+"))
plus.grid(row=1, column = 3 , padx=5 ,pady=5)
minus = ctk.CTkButton(frame, text="-", fg_color="black", width=100, height=100, font=("",40),command=lambda:equation_display("-"))
minus.grid(row=2, column = 3 , padx=5 ,pady=5)
multiply = ctk.CTkButton(frame, text="*", fg_color="black", width=100, height=100, font=("",40),command=lambda:equation_display("*"))
multiply.grid(row=1, column = 4 , padx=5 ,pady=5)
divide = ctk.CTkButton(frame, text="/", fg_color="black", width=100, height=100, font=("",40),command=lambda:equation_display("/"))
divide.grid(row=2, column = 4 , padx=5 ,pady=5)
equal = ctk.CTkButton(frame, text="=", fg_color="black", width=100, height=100, font=("",40),command=lambda:equation_display("="))
equal.grid(row=0, column = 4 , padx=5 ,pady=5)





app.mainloop() #เปิดขึ้นมา