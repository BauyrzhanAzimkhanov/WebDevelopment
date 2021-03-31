def xyz_there(string):
    if(string.count('xyz') - string.count('.xyz') >= 1):
        return True
    return False