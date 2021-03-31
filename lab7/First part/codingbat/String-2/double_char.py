def double_char(string):
  ans = ''
  for i in range(len(string)):
    ans = ans + string[i] + string[i]
  return ans