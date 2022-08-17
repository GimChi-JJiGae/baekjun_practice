
testcase = int(input())
for tc in range(1, testcase + 1):
    N = int(input())
    print(f"#{tc}")
    pascal = [[] for i in range(N)]                                         # 삼각형 안의 숫자 정보를 저장할 2차원 리스트
    length = 1                                                              # 삼각형 층마다의 가로길이, 내려갈수록 1씩 늘어남
    for i in range(N):
        for j in range(length):
            if j == 0 or j == length - 1:                                   # 한 행의 양 끝은 1이다
                pascal[i].append(1)
            else:
                pascal[i].append(pascal[i - 1][j - 1] + pascal[i - 1][j])   # 삼각형 안의 특정 값은 위의 두 값의 합이다.
        length += 1
        print(*pascal[i])                                                   # 한 줄씩 출력


