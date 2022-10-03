def perm(n, now, k):
    if now == k:
        temp = tuple(result)
        total.append(temp)
    else:
        for i in range(n):
            result[now] = arr[i]
            perm(n, now + 1, k)
            result[now] = 0

N, M = map(int, input().split())
arr = list(map(int, input().split()))
result = [0] * M
total = []
perm(N, 0, M)
total = list(set(total))
total.sort()

for i in range(len(total)):
    print(*total[i])