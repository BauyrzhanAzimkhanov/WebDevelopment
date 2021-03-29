a = int(input())
ans = 0
cnt = 0
while(a > 0):
    ans = ans + (a % 10) * 2**(cnt)
    cnt += 1
    a = a // 10
print(ans)