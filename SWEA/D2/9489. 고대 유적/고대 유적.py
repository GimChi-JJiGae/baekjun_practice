

test_case = int(input())

for tc in range(1, test_case + 1):
    N, M = map(int, input().split())
    max_len = 0
    land = []
    for i in range(N):
        land.append(list(map(int, input().split())))
    transposed_land =[[] for i in range(M)]
    for j in range(M):
        for i in range(N):
            transposed_land[j].append(land[i][j])

    #transposed_land = np.transpose(land)                # 전치 행렬, 행과 렬이 바뀐 행렬이다. for문을 적게 돌기 위함
    for i in range(N):                                  # 가로 기준으로 기존 행렬과 전치행렬을 동시에 확인한다
        count1 = 0                                      # 기존 행렬용 count
        for j in range(M):
            if land[i][j] == 1:
                count1 += 1                             # 1이 나올 경우 count를 +1 해준다.
                if count1 > max_len:
                    max_len = count1
            else:
                count1 = 0                              # 1이 더 없을 경우 0
    for j in range(M):
        count2 = 0
        for i in range(N):
            if transposed_land[j][i] == 1:
                count2 += 1
                if count2 > max_len:
                    max_len = count2
            else:
                count2 = 0
    print(f"#{tc} {max_len}")