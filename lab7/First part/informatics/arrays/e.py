import array as arr
n = int(input())
a = []
a = input().split(" ")
ans = 'NO'
for i in range(1, n):
    if((int(a[i]) >= 0 and int(a[i-1]) >= 0) or (int(a[i]) < 0 and int(a[i-1]) < 0)):
        ans = 'YES' 
print(ans)