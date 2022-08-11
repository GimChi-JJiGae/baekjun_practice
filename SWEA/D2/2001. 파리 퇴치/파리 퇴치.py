
testcase = int(input())

for tc in range(testcase):
    N, M = map(int, input().split())
    matrix = []
    for i in range(N):
        matrix.append(list(map(int, input().split())))  # 파리 수가 각방에 들어있는 이차원 배열

    max_sum = 0
    for i in range(N - M + 1):          # 파리채가 움직일 수 있는 가로 범위
        for j in range(N - M + 1):      # 파리채가 움직일 수 있는 세로 범위
            Sum = 0
            for k in range(M):                 # 파리채 가로범위
                for l in range(M):             # 파리채 세로범위
                   Sum += matrix[i + k][j + l]
            if Sum > max_sum:
                max_sum = Sum
    print(f"#{tc + 1} {max_sum}")
