while True:
    mm_dd_yy = input("type mm/dd/yyyy(12/20/2006):")
    if mm_dd_yy.isdigit() or mm_dd_yy.isspace() :
        print ("error")
    else:
        month_str = ["","JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]
        date = mm_dd_yy.split("/") # ["12", "20", "2006"]
        date[0] = int(date[0])
        if date[0] > 12 or date[0] < 1:
            print ("error")
            continue
        else: 
            print(f"{date[1]} {month_str[date[0]]} {date[2]} ")
            break