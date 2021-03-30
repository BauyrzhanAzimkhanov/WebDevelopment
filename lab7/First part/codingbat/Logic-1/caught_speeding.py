def caught_speeding(speed, is_birthday):
    if((is_birthday == True and speed <= 65) or (is_birthday == False and speed <= 60)):
        return(0)
    if((is_birthday == True and speed <= 85) or (is_birthday == False and speed <= 80)):
        return(1)
    return(2)