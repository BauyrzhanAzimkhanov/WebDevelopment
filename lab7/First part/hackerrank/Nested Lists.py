n = int(input())
lis = []
min1 = 900000
min2 = 1000000
min1_n = ''
min2_n = []
ans = []
for i in range(n):
    a = input()
    b = float(input())
    lis.append([a, b])
    if(b < min1):
        min2 = min1
        min2_n = min1_n
        min1 = b
        min1_n = a
    elif(b < min2 and b > min1):
        min2 = b
        min2_n = a
print(min2)
for i in range(len(lis[i])):
    if(lis[i][1] == min2):
        ans.append(lis[i][0])
ans.sort()
for i in ans:
    print(i)

