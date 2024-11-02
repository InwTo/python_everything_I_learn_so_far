date = {"mm":0,"dd":0,"yy":0,}
while True:
    mm_dd_yy = (input("type mm/dd/yyyy(12/20/2006):"))
    if mm_dd_yy.isdigit() or mm_dd_yy.isspace() :
        print ("error")
    else:
        mm_dd_yy2=mm_dd_yy.split("/")
        date["mm"]=mm_dd_yy2[0]
        date["mm"]=int(date["mm"])
        date["dd"]=mm_dd_yy2[1]
        date["dd"]=int(date["dd"])
        date["yy"]=mm_dd_yy2[2]
        date["yy"]=int(date["yy"])
        print(date)
        if date["mm"] > 12 or date["dd"] < 1:
            print ("error")
        elif date["mm"] == 1:
            date["mm"] = ("Jan")
        elif date["mm"] == 2:
            date["mm"] = ("Feb")
        elif date["mm"] == 3:
            date["mm"] = ("Mar")
        elif date["mm"] == 4:
            date["mm"] = ("Apr")
        elif date["mm"] == 5:
            date["mm"] = ("May ")
        elif date["mm"] == 6:
            date["mm"] = ("Jun")
        elif date["mm"] == 7:
            date["mm"] = ("Jul")
        elif date["mm"] == 8:
            date["mm"] = ("Aug")
        elif date["mm"] == 9:
            date["mm"] = ("Sept")
        elif date["mm"] == 10:
            date["mm"] = ("Oct")
        elif date["mm"] == 11:
            date["mm"] = ("Nov")
        elif date["mm"] == 12:
            date["mm"] = ("Dec")
        else:
            print("something is wrong bro")
        print(f"{date['dd']} {date['mm']} {date['yy']} ")
        break







