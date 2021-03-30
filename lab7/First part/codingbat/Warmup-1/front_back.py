def front_back(string):
    if(len(string) <= 1):
      return string
    return(string[len(string) - 1] + string[1: len(string) - 1] + string[0])