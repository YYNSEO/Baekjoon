X = int(input())
N = int(input())
r = []
for i in range (0, N):
    a, b = map(int, input().split())
    result = a * b
    r.append(result)

results = sum(r)
if X == results:
    x = "Yes"
    print(x)
else:
    x = "No"
    print(x)

