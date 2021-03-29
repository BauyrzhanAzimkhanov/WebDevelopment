n = int(input())
s = input().split()
max = int(-1000)
max2 = int(-1500)
for i in range(1, n):
    if(int(s[i]) > max):
        max2 = int(max)
        max = int(s[i])
    elif(int(s[i]) > max2 and int(s[i]) < max):
        max2 = int(s[i])
print(max2)