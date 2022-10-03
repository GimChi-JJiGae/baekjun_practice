def comb(N, r, s):
    if r == 0:
        tmp = made[:]
        tmp.sort()
        print(*tmp)
    else:
        for i in range(s, N - r + 1):
            made[r - 1] = arr[i]
            comb(N, r-1, i+1)
            made[r - 1] = 0


N, M = map(int, input().split())
arr = list(range(1, N + 1))
made = [0] * M
comb(N, M, 0)