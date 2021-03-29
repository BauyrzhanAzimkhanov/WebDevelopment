a = int(input())
i = a
ans = a
while(i > 1):
    if(a % i == 0):
        ans = i
    i -= 1
print(ans)