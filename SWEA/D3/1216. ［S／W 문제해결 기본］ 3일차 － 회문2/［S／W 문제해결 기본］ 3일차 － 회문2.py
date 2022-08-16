
for tests in range(10):
    tc = int(input())

    matrix = []
    for line in range(100):
        matrix.append(list(input()))

    max_len = 1                                                     # 최장 회문 길이
    for i in range(100):
        for j in range(100):
            break1 = False                                          # 행(가로)에 대한 종료 확인 True 시 종료
            break2 = False                                          # 열(세로)에 대한 종료 확인 True 시 종료

            if j + 1 < 100 and matrix[i][j] == matrix[i][j + 1]:    # 짝수 가로 회문 확인, and 앞 조건이 만족하면 and 뒤 인덱스 에러가 없음
                len = 2
                k = 1
                while(not break1):                                  # 가로 회문 검사가 진행 중일 때
                    try:
                        if matrix[i][j - k] == matrix[i][j + 1 + k]: # 양 옆으로 한 칸씩 더 보았을 때 회문인 경우
                            len += 2
                            k += 1
                        else:
                            break1 = True                           # 회문이 아니라면 탈출
                    except IndexError:                              # matrix를 벗어나는 인덱스 에러일 경우도 탈출
                        break1 = True
                if len > max_len:
                    max_len = len                                   # 최장 회문 갱신시 값 갱신

            break1 = False                                          # 나중에 다시 쓰기 위해 값을 초기화


            if i + 1 < 100 and matrix[i][j] == matrix[i + 1][j]:    # 짝수 세로 회문 확인
                len = 2
                k = 1
                while(not break2):
                    try:
                        if matrix[i - k][j] == matrix[i + 1 + k][j]: # 위 아래로 한 칸씩 더 보았을 떄 회문인 경우
                            len += 2
                            k += 1
                        else:
                            break2 = True                           # 회문이 아니라면 탈출
                    except IndexError:
                        break2 = True
                if len > max_len:
                    max_len = len

            break2 = False

            len_x = 1                                               # 홀수 길이 회문 확인을 위한 값 초기화
            len_y = 1
            k_x = 0                                                 # 가로 인덱스에 더하고 빼줄 k 값
            k_y = 0                                                 # 세로 인덱스에 더하고 빼줄 k 값

            while(True):                                            # 홀수 길이는 가로와 세로를 동시에 확인함
                if break1 and break2:                               # 가로 세로에서 더 이상 회문을 찾을 수 없을 때 빠져나옴
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

