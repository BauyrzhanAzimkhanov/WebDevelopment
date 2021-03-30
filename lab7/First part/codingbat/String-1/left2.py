def left2(string):
    if(len(string) <= 2):
        return string
    else:
        return string[2:] + string[:2]