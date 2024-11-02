"""
    เขียนโปรแกรม รับเลขจำนวนเต็ม 1 จำนวน (n)
    จากนั้น ให้หาผลรวมของเลขตั้งแต่ 1-n
    โดยผลรวมจะให้แยกเป็นผลรวม เลขคู่ และผลรวมเลขคี่

    Enter number: 10

    sum odd = 1+3+5+7+9 = ?
    sum even = 2+4+6+8+10 = ?
"""
n=int(input("number:"))
sum1=0
sum2=0
if n==0 or n < 0:
    print("error")     
else:
    for i in range (1, n+1 ,2):
        sum1=sum1+i
        print(sum1)
    print(".")
    for i in range (2, n+1,2):
        sum2=sum2+i
        print(sum2)
print(f"sum odd ={sum1}")
print(f"summ even={sum2}")














