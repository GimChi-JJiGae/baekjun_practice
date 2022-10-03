def perm(n, now, k):
    if now == k:
        print(*result)
    else:
        for i in range(n):
            result[now] = arr[i]
            perm(n, now + 1, k)
            result[now] = 0

N, M = map(int, input().split())
arr = list(range(1, N + 1))
result = [0] * M
perm(N, 0, M)
