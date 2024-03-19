A, B = map(int, input().split())
C = int(input())
a = A*60
b = a+B+C
c = b//60
d = b%60
if c >= 24:
    e = c-24
    print(e, d)
else:
    print(c, d)