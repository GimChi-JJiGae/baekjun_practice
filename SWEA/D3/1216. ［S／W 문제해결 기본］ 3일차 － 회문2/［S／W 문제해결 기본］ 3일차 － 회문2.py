
for tests in range(10):
    tc = int(input())

    matrix = []
    for line in range(100):
        matrix.append(list(input()))

    max_len = 1                                 # 최장 회문 길이
    for i in range(100):
        for j in range(100):
            break1 = False                      # 행에 대한 종료 확인
            break2 = False                      # 열에 대한 종료 확인


            if j + 1 < 100:
                if matrix[i][j] == matrix[i][j + 1]:    # 짝수 가로 회문 확인
                    len = 2
                    k = 1
                    while(not break1):
                        try:
                            if matrix[i][j - k] == matrix[i][j + 1 + k]:
                                len += 2
                                k += 1
                            else:
                                break1 = True
                        except IndexError:
                            break1 = True
                    if len > max_len:
                        max_len = len

            break1 = False                          # 다시 쓰기 위해 값 초기화

            if i + 1 < 100:
                if matrix[i][j] == matrix[i + 1][j]:    # 짝수 세로 회문 확인
                    len = 2
                    k = 1
                    while(not break2):
                        try:
                            if matrix[i - k][j] == matrix[i + 1 + k][j]:
                                len += 2
                                k += 1
                            else:
                                break2 = True
                        except IndexError:
                            break2 = True
                    if len> max_len:
                        max_len = len

            break2 = False

            len_x = 1                                 # 홀수 길이 회문 확인을 위한 값 초기화
            len_y = 1
            k_x = 0
            k_y = 0

            while(True):                            # 홀수 길이는 가로와 세로를 동시에 확인함
                if break1 and break2:
                    break

                try:
                    if not break1:
                        if matrix[i][j - 1 - k_x] == matrix[i][j + 1 + k_x]:    # 가로 회문 확인
                            len_x += 2
                            k_x += 1
                        else:
                            break1 = True
                except IndexError:
                    break1 = True

                try:
                    if not break2:
                        if matrix[i - 1 - k_y][j] == matrix[i + 1 + k_y][j]:    # 세로 회문 확인
                            len_y += 2
                            k_y += 1
                        else:
                            break2 = True
                except IndexError:
                    break2 = True

            if len_x > max_len:
                max_len = len_x
            if len_y > max_len:
                max_len = len_y

    print(f'#{tc} {max_len}')

