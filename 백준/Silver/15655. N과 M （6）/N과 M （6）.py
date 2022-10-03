def comb(n, r, start):
    if r == 0:
        temp = made[:]
        temp.sort()
        print(*temp)
    else:
        for j in range(start, n-r+1):
            made[r - 1] = arr[j]
            comb(n, r-1, j+1)
            made[r - 1] = 0



N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
made = [0] * M
comb(N, M, 0)