testcase = 10

for tc in range(1, testcase + 1):
    length = int(input())
    matrix = [[] for i in range(8)]
    for i in range(8):
        matrix[i] = matrix[i] + list(input())

    total = 0
    for i in range(8):
        for j in range(8):
            if length % 2 == 1:                 # 홀수일 때
                if j - length // 2 >= 0 and j + length // 2 < 8:    # 가로 회문 확인
                    for k in range(1, length // 2 + 1):
                        if matrix[i][j - k] == matrix[i][j + k]:
                            continue
                        else:
                            break
                    else:

                        total += 1

                if i - length // 2 >= 0 and i + length // 2 < 8:  # 세로 회문 확인
                    for k in range(1, length // 2 + 1):
                        if matrix[i - k][j] == matrix[i + k][j]:
                            continue
                        else:
                            break
                    else:

                        total += 1

            else:                               # 짝수일 때
                if j - (length // 2 - 1) >= 0 and j + length // 2 < 8:
                    if matrix[i][j] == matrix[i][j + 1]:
                        for k in range(1, length // 2):
                            if matrix[i][j - k] == matrix[i][j + k + 1]:
                                continue
                            else:
                                break
                        else:

                            total += 1
                    else:
                        pass

                if i - (length // 2 - 1) >= 0 and i + length // 2 < 8:
                    a = matrix[i][j]
                    b = matrix[i + 1][j]
                    if matrix[i][j] == matrix[i + 1][j]:
                        for k in range(1, length // 2):
                            if matrix[i - k][j] == matrix[i + k + 1][j]:
                                continue
                            else:
                                break
                        else:
                            total += 1
                    else:
                        pass

    print(f"#{tc} {total}")
