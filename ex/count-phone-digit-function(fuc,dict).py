"""
    input phone number: 0811332555

    0 = ?
    1 = ?
    2 = ?
    3 = ?
    4 = ?
    5 = ?
    6 = ?                                                                        
    7 = ?
    8 = ?
    9 = ?
"""

def collect_num(phone_number1):
    phone_value = {"0":0, "1":0, "2":0 ,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0}
    for i in range (len(phone_number1)):
        phone_value[phone_number1[i]]=phone_value[phone_number1[i]]+1
    return phone_value




def print_all(phone_value2):
    for key in (phone_value2):
        print(f"{key} = {phone_value2[key]}")




def max_count_and_value(phone_value3):
    max_count=0
    max_value=0
    for key in  (phone_value3):
        if phone_value3[key] > max_count:
            max_count = phone_value3[key]
            max_value = key
            return max_count, max_value



phone_number2 = input("phonenumber for count how many each number:")
phone_value_input=collect_num(phone_number2)
print_all(phone_value_input)
a,b=max_count_and_value(phone_value_input)

print(f"mode={b}({a})")


