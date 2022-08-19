
testcase = 10
for tc in range(1, testcase + 1):
    num = int(input())
    matrix = [[] for i in range(num)]


    for i in range(100):
        _line = list(map(int, input().split()))         # 100 x 100 matrix를 만들어둔다
        matrix[i] = matrix[i] + _line

    total_count = 0                                     # 전체 교착 상태 갯수
    for j in range(100):                                # 특정 열에서 행을 하나씩 살펴본다

        check_N = True                                  # N을 찾아야함
        check_S = False                                 # S를 찾아야함

        for i in range(100):
            if check_N:
                if matrix[i][j] == 1:                   # N을 찾은 경우
                    check_S = True
                    check_N = False
            elif check_S:
                if matrix[i][j] == 2:                   # S를 찾은 경우, NS 순서로 세로로 있을 때 교착상태 형성
                    check_N = True
                    check_S = False
                    total_count += 1

    print(f"#{tc} {total_count}")

