def alarm_clock(day, vacation):
    if(vacation == True):
        if(day <= 5 and day > 0):
            return('10:00')
        else:
            return('off')
    else:
        if(day <= 5 and day > 0):
            return('7:00')
        else:
            return('10:00')