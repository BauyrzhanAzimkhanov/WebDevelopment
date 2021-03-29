x = int(input())
d = int(input())
cnt = 0
ans = 0

i = x
while(i > 0):
    if(i % 10 == d):
        ans += 1
    i = i // 10

    
print(ans)