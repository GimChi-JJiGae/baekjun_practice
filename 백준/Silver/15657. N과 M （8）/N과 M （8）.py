def perm(n, now, k):
    if now == k:
        print(*result)
    else:
        for i in range(n):
            result[now] = arr[i]
            if now > 0:
                if result[now] < result[now - 1]:
                    result[now] = 0
                    continue

            perm(n, now + 1, k)
            result[now] = 0

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
result = [0] * M
perm(N, 0, M)
