def front_times(string, n):
    if(len(string) < 3):
        return string * n
    return string[:3] * n