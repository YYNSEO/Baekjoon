H, M = map(int, input().split())
h = H*60
m = h+M-45
c = m//60
d = m%60
if c == -1:
    c = 23
print(c, d)
