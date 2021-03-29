a = int(input())
b = int(input())
c = int(input())
if(a < c and b < c):
   print(3)
elif(b < a and c < a):
    print(1)
elif(c < b and a < b):
    print(2)