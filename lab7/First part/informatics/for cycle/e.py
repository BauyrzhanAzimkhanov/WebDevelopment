a = int(input())
i = a
ans = 0
while(i > 0):
    ans = ans + i % 10
    i //= 10
print(ans)