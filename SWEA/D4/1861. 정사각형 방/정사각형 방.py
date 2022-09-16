
testcase = int(input())
for tc in range(1, testcase + 1):
    N = int(input())
    matrix = [None] * N
    for i in range(N):
        matrix[i] = list(map(int, input().split()))     # 데이터 입력 받기

    d = [[-1, 0], [0, 1], [1, 0], [0, -1]]

    cord_dict = {}
    for i in range(N):
        for j in range(N):
            cord_dict[matrix[i][j]] = [i, j]            # 칸 안의 값을 키 값으로 좌표를 저장하는 딕셔너리

    best_start = matrix[0][0]
    best_depth = 1

    skipline = 0
    for i in range(1, N**2):

        if skipline:
            skipline -= 1
            continue

        if best_depth > (N**2 - i):
            break

        start_i = cord_dict[i][0]
        start_j = cord_dict[i][1]
        may_be = i
        depth = 1
        now = i
        while(1):
            for j in d:
                try:
                    if matrix[start_i + j[0]][start_j + j[1]] == now + 1:   # 주위에 자기보다 1 만큼 큰 칸이 있다면
                        start_i = start_i + j[0]
                        start_j = start_j + j[1]
                        depth += 1
                        now = matrix[start_i][start_j]
                        break
                except IndexError:
                    continue

            else:
                break

        if depth > best_depth:
            best_depth = depth
            best_start = may_be
        skipline = depth - 1

    print(f"#{tc} {best_start} {best_depth}")









