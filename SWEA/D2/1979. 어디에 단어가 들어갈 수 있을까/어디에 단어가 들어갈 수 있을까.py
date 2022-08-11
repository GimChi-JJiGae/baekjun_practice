
testcase = int(input())

for tc in range(1, testcase + 1):
    N, K = map(int, input().split())
    matrix = []
    for i in range(N):
        matrix.append(list(map(int, input().split())))
    count = 0
    total_count = 0
    for i in range(N):                              # 가로 확인

        if count == K:
            total_count += 1                        # 줄이 바뀔 때 count를 단어길이에 딱 맞게 채웠는지도 확인해야한다.
        count = 0
        for j in range(N):
            if matrix[i][j] == 0:
                if count == K:                      # 검은 부분이라면 그전 까지의 카운트가 단어 길이와 같은지 확인
                    total_count += 1                # 같을 경우 단어를 넣을 수 있는 공간 + 1
                    count = 0
                else:                               # 아닐 경우 다시 그냥 다시 초기화
                    count = 0
            else:
                count += 1

    for j in range(N):                              # 세로 확인

        if count == K:                              # 가로의 마지막 부분은 여기서도 체크가 된다.
            total_count += 1
        count = 0
        for i in range(N):
            if matrix[i][j] == 0:
                if count == K:
                    total_count += 1
                    count = 0
                else:
                    count = 0
            else:
                count += 1
    if count == K:
        total_count += 1                            # 마지막에 부분에서 체크가 안될수도있으니 확인
    print(f"#{tc} {total_count}")