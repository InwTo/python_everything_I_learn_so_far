import tkinter as tk
import customtkinter as ctk

def calculate(operator: str): 
   #ทำบวกลบคูณหาร
    entry_value1 = eval(entry1.get())#อันนี้คือคำสั่งเอาไว้แบบดึงเข้ามาในฟังก์ชั่น 
    entry_value2 = eval(entry2.get())#เหมือนอันนี้มันก็ดึงจากentry(ที่พิม)มาในฟังชั่นเพื่อบวก
    if operator == "+":
        result = entry_value1 + entry_value2
    elif operator == "-":
        result = entry_value1 - entry_value2
    elif operator == "*":
        result = entry_value1 * entry_value2
    elif operator == "/":
        result = entry_value1 / entry_value2
    result_label.configure(text=f"Result: {result:.2f}")#configureคือเปลี่ยน
    
    




app = ctk.CTk() # create new window

app.geometry("1080x720") # set width x height of window
app.title("Calculator")

header = ctk.CTkLabel(app, text="Calculator", fg_color="transparent", font=("", 60)) # create text

# padx = padding x axis (spacing of UI)
# pady = padding y axis
header.pack(padx=50, pady=50) # show this UI 

input_frame = ctk.CTkFrame(app, fg_color="transparent") # create a row
input_frame.pack()

label1 = ctk.CTkLabel(input_frame, text="first number: ", fg_color="transparent" ,font=("",36))
label1.grid(row=0, column=0, padx=10, pady=0)
entry1 = ctk.CTkEntry(input_frame, width=350, height=50, font=("", 36))
entry1.grid(row=0, column=1)

#ตอนนึี้ทำปุ่มกด แล้วก็มีกล่อง2กล่อง 
label2 = ctk.CTkLabel(input_frame, text="second number: ",fg_color="transparent" ,font=("",36))
label2.grid(row=1, column=0, padx=10, pady=50)
entry2 = ctk.CTkEntry(input_frame, width=350, height=50, font=("",36))
entry2.grid(row=1, column=1)


inpt_frame2 = ctk.CTkFrame(app,fg_color="transparent")
inpt_frame2.pack(pady=50)

plus_button = ctk.CTkButton(inpt_frame2, text="+", command=lambda: calculate("+")  , width=150 , height=50 ,font=("",50))#lambda คือเอาไว้ใช้เรียกฟังชั่นในcommardต้องมีมันก่อนถึงจะเรียกได้
plus_button.grid(row=0, column=0 ,padx=10)

minus_button = ctk.CTkButton(inpt_frame2, text="-", command=lambda: calculate("-") , width=150 , height=50 ,font=("",50))
minus_button.grid(row=0, column=1 ,padx=10)

multiplied_button = ctk.CTkButton(inpt_frame2, text="*", command=lambda:calculate("*"), width=150 , height=50 ,font=("",50))
multiplied_button.grid(row=0, column=2 ,padx=10)

divide_button = ctk.CTkButton(inpt_frame2, text="/", command=lambda:calculate("/") , width=150 , height=50 ,font=("",50))
divide_button.grid(row=0, column=3 ,padx=10)

result_label = ctk.CTkLabel(app, text="result: ", fg_color="transparent" ,font=("",36))
result_label.pack(pady=50)



app.mainloop() # show window
