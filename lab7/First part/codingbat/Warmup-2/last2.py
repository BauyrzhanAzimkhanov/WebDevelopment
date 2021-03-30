def last2(string):
    if(len(string) < 2):
        return 0
    last2 = string[len(string)-2:]
    count = 0
  
    for i in range(len(string)-2):
        sub = string[i:i+2]
        if(sub == last2):
            count = count + 1

    return count