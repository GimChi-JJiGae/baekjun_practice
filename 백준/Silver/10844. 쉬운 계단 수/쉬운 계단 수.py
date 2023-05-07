n = int(input())

# 초기값 설정
dp = [[0] * 10 for _ in range(n+1)]
for i in range(1, 10):
    dp[1][i] = 1

# 점화식을 이용한 계산
for i in range(2, n+1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][j+1]
        elif j == 9:
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

# 결과 출력
print(sum(dp[n]) % 1000000000)