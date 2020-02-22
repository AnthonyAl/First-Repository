from datetime import datetime

def monthtodays(r,s,v):
    global md
    if(r==1):
        md=31
        return v
    elif(r==2):
        md=s
        return 31 + v
    elif(r==3):
        md=31
        return 31 + s + v
    elif(r==4):
        md=30
        return 31*2 + s + v
    elif(r==5):
        md=31
        return 31*2 + s + 30 + v
    elif(r==6):
        md=30
        return 31*3 + s + 30 + v
    elif(r==7):
        md=31
        return 31*3 + s + 30*2 + v
    elif(r==8):
        md=31
        return 31*4 + s + 30*2 + v
    elif(r==9):
        md=30
        return 31*5 + s + 30*2 + v
    elif(r==10):
        md=31
        return 31*5 + s + 30*3 + v
    elif(r==11):
        md=30
        return 31*6 + s + 30*3 + v
    elif(r==12):
        md=31
        return 31*6 + s + 30*4 + v

while(True):
    now = datetime.now()
    print("now =", now)

    give=input("Give a date in the form HH/MM/EEEE,\nor type 'stop' to exit the algorithm:\n")
    if(give=="stop" or give=="STOP" or give=="Stop" or give=="'stop'"):
        break
    then=give.split("/")
    print(then, "\n")

    today=now.strftime("%d")

    thismonth=now.strftime("%m")

    thisyear=now.strftime("%Y")

    thishour=now.strftime("%H")

    thisminute=now.strftime("%M")

    thissecond=now.strftime("%S")

    u=0
    y=int(then[2])-int(thisyear)
    if(y<0):
        u=1

    if(u==1):
        xx=int(thisyear)
        yy=int(then[2])
    else:
        xx=int(then[2])
        yy=int(thisyear)

    sy=0

    for i in range(yy,xx):
        if(i%4==0 and i%100!=0 or i%400==0):
            sy+=366
        else:
            sy+=365

    m1=int(thismonth)
    m2=int(then[1])
    d1=int(today)
    d2=int(then[0])
    sm1=28
    sm2=28
    
    if(m1==2):
        if(int(thisyear)%4==0 and int(thisyear)%100!=0 or int(thisyear)%400==0):
            sm1=29

    if(m2==2):
        if(int(then[2])%4==0 and int(then[2])%100!=0 or int(then[2])%400==0):
            sm2=29


    dom1=monthtodays(m1,sm1,d1)
    dom2=monthtodays(m2,sm2,d2)

    dom=dom1-dom2
    
    y=sy+dom

    if(y<0):
        y=-y
    #Ακολουθεί ό,τι κατάλαβα από την εκφώνηση... :/
    h=y*24+int(thishour)

    mi=h*60+int(thisminute)

    sec=mi*60+int(thissecond)

    print("The time gap; \nin days: ", y, "\nin hours: ", h, "\nin seconds: ", sec, "\nThe month of the given date has ", md, " days in total.\n\n")

print("Exiting. . .\n\n")