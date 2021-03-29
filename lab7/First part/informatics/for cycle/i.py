import math
a = int(input())
ans = 0
for i in range(1, math.ceil(a / 2) + 1):
    if(a % i == 0):
        #print(i)
        ans += 1
print(ans + 1, end="")