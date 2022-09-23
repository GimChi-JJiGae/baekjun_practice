testcase = int(input())


for tc in range(1, testcase + 1):
    N = int(input())
    matrix = []
    for i in range(N):
        matrix.append(list(map(int, input().split())))

    max_length = -1

    for i in range(N):
        for j in range(N):

            # 행렬안의 숫자를 하나씩 돌며 시계방향으로 체크할 예정이다.
            # 가장 작은 사각형부터, 벽에 닿을 크기의 사각형까지 확인할 것이다.

            for k in range(1, min(i, N - (j + 1)) + 1):                         # 위, 오른쪽 중 가까운 거리 만큼
                for l in range(1, min(N - (i + 1), (N - (j + k + 1))) + 1):     # 아래, 오른쪽 중 가까운 거리만큼
                    if (k + l) * 2 < max_length:                                # 만들려는 사각형이 이미 최댓값보다 작다.
                        continue
                    way = [0 for _ in range(2*(l+k))]                           # 지나간 값들을 여기에 저장
                    new_i = i
                    new_j = j
                    way[0] = matrix[new_i][new_j]
                    num = 1
                    for a in range(1, k + 1):
                        new_i = new_i - 1
                        new_j = new_j + 1
                        way[num] = matrix[new_i][new_j]
                        num += 1
                    for b in range(1, l + 1):
                        new_i = new_i + 1
                        new_j = new_j + 1
                        way[num] = matrix[new_i][new_j]
                        num += 1
                    for c in range(1, k + 1):
                        new_i = new_i + 1
                        new_j = new_j - 1
                        way[num] = matrix[new_i][new_j]
                        num += 1
                    for d in range(1, l):
                        new_i = new_i - 1
                        new_j = new_j - 1
                        way[num] = matrix[new_i][new_j]
                        num += 1

                    len_a = len(way)
                    len_b = len(set(tuple(way)))        # 중복이 있는지를 확인하기 위함
                    if len_a == len_b:                  # 중복이 없으면 최대 길이를 확인한다.
                        if max_length < len_a:
                            max_length = len_a
    print(f"#{tc} {max_length}")





