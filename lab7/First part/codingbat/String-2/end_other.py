def end_other(a, b):
    temp1 = a.lower()
    temp2 = b.lower()
    return(temp1.endswith(temp2) or temp2.endswith(temp1))