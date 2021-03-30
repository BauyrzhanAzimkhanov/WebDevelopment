def not_string(string):
    if(string.find('not') == 0):
        return string
    return 'not ' + string