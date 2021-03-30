def combo_string(a, b):
    mini = 0
    if(len(a) < len(b)):
        return a + b + a
    else:
        return b + a + b