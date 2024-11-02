"""
    เขียนโปรแกรมรับค่า ประโยค 1 ประโยค
    จากนั้นให้นำประโยคดังกล่าวมาแยกออกเป็นคำๆ และนับว่า แต่ละคำมีซ้ำกี่ครั้งในประโยค
    และพิมพ์คำที่นับได้ออกทางหน้าจอ

    enter text: This is a cat, my name is aungkoon, my cat love food.

    This = 1
    is = 2
    a = 1
    cat = 2
    my = 2
    name = 1
    aungkoon = 1
    love = 1
    food = 1

    max words = is (2)
    
"""

word_intaker = input ("enter text:")
word_intaker = word_intaker.replace(",","").replace(".","")
word_intaker2 = word_intaker.split(" ")
print(word_intaker2)
words_count = {}


# loop for count words
for i in range(len(word_intaker2)): # {"A": 1, "B": 4, "C":10, "D":11}
    if word_intaker2[i] in words_count.keys():#.key()ใช้อย่างข้อนี้ที่ว่าถ้ามีชื่อซ้ำกับkeyของwordcountก็+1 สามารถใช้.value()ได้ด้วย
        words_count[word_intaker2[i]]=words_count[word_intaker2[i]]+1
    else:
        words_count[word_intaker2[i]] = 1

# loop for print
for key in words_count:
    print (f"{key}={words_count[key]}")




max_word2=0
max_value2=0
# loop find max words
for key in  (words_count):
    if words_count[key]>max_word2:
        max_word2=words_count[key]
        max_value2=key

# loop find same
# max word = this, is, a (2)
print_list = []

for key in  (words_count):
    if words_count[key]==max_word2:
        print_list.append(key)

print_list2 =(str(print_list))
print_list_no_double_quote=print_list2.replace(" " " "," ")

print_str = ""
for key in  (words_count):
    if words_count[key]==max_word2:
        print_str = print_str + key + ", "#มันเก็บตัวก่อนไว้แบบthis จากนั้นเพิ่มis
        #ปัญหาคือthis,is,(2)มี,เกินมา

count_str=len(print_str)
print(f"maxword = {print_str[0:count_str-2]} ({max_word2})")




    







