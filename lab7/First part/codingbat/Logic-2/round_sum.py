def round10(num):
    if(num % 10 <= 4):
        return num - (num % 10)
    else:
        return num + (10 - (num % 10))
def round_sum(a, b, c):
    return(round10(a) + round10(b) + round10(c))