def perm(n, now, k):
    if now == k:
        print(*result)
    else:
        for i in range(n):
            if not used[i]:
                result[now] = arr[i]
                used[i] = 1
                perm(n, now + 1, k)
                result[now] = 0
                used[i] = 0

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
result = [0] * M
used = [0] * N
perm(N, 0, M)
