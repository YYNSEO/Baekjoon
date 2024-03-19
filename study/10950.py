T = int(input())
c=[]
# for i in range(0, T):
#     A, B = map(int, input().split())
#     d = A + B
#     c.append(d)
# for j in range(0, T):
#     print(c[j])

a = 0
while a < T:
    a += 1
    A, B = map(int, input().split())
    d = A + B
    c.append(d)

z = 0
while z < T:
    print(c[z])
    z += 1
