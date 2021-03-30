def without_end(string):
    if(len(string) < 3):
        return ''
    else:
        return string[1: len(string) - 1]