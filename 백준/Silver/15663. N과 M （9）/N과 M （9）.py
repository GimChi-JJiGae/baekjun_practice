def perm(n, now, k):
    if now == k:
        temp = result[:]
        total.append(tuple(temp))
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
total = []

result = [0] * M
used = [0] * N
perm(N, 0, M)
total = list(set(total))
total.sort()
for i in range(len(total)):
    print(*total[i])
