while True:
    mm_dd_yy = input("type mm/dd/yyyy(12/20/2006):")
    if mm_dd_yy.isdigit() or mm_dd_yy.isspace() :
        print ("error")
    else:
        date = mm_dd_yy.split("/") # ["12", "20", "2006"]
        date[0] = int(date[0])
        if date[0] > 12 or date[0] < 1:
            print ("error")
            continue
        elif date[0] == 1:
            date[0] = "Jan"
        elif date[0] == 2:
            date[0] = "Feb"
        elif date[0] == 3:
            date[0] = "Mar"
        elif date[0] == 4:
            date[0] = "Apr"
        elif date[0] == 5:
            date[0] = "May"
        elif date[0] == 6:
            date[0] = "Jun"
        elif date[0] == 7:
            date[0] = "Jul"
        elif date[0] == 8:
            date[0] = "Aug"
        elif date[0] == 9:
            date[0] = "Sep"
        elif date[0] == 10:
            date[0] = "Oct"
        elif date[0] == 11:
            date[0] = "Nov"
        elif date[0] == 12:
            date[0] = "Dec"
        else:
            print("something is wrong bro")
        print(f"{date[1]} {date[0]} {date[2]} ")
        break
        