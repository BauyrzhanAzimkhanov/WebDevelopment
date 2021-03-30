def string_match(a, b):
    mini = 0
    ans = 0
    if(len(a) < len(b)):
        mini = len(a)
    else:
        mini = len(b)
    for i in range(mini - 1):
        if(a[i] == b[i] and a[i+1] == b[i+1]):
            ans += 1
    return ans