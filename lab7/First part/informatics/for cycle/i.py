import math
n = int(input())
k = 0
for i in range(1, math.floor(math.sqrt(n + 1))):
    if n%i==0:
        k+=2
 
print(k)