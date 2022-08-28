
testcase = int(input())
for tc in range(1, testcase + 1):
    N = int(input())
    maxtrix = []
    for i in range(N):
        maxtrix.append(list(input()))



    L1 = 0
    L2 = 0
    total = 0
    for i in range(N // 2):
        for j in range(N // 2 - L1, N//2 + L1 + 1):

            total += int(maxtrix[i][j])
        L1 += 1

    for i in range(N // 2, N):
        for j in range(0 + L2, N - L2):
            total += int(maxtrix[i][j])
        L2 += 1

    print(f"#{tc} {total}")




