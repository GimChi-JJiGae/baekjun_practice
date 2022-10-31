total = int(input())
N = int(input())
new_total = 0
for i in range(N):
    a, b = map(int, input().split())
    new_total += a * b
if total == new_total:
    print('Yes')
else:
    print('No')