
N, M = map(int, input().split())      # N이 사람 수, M이 놀이기구 수
time = list(map(int, input().split()))

#운영 시간으로 이분탐색

if N < M:
    print(N)
else:
    left = 0
    right = 60000000000
    t = right
    while left <= right:
        mid = (left + right) // 2
        cnt = M             # 시간 초과시에도 타고 있을 수 있으니 일단 하나씩 넣어두자
        for i in range(M):
            cnt += mid // time[i]
        if cnt >= N:
            t = mid
            right = mid - 1
        else:
            left = mid + 1

        cnt = M
    for i in range(M):
        cnt += (t - 1) // time[i]
    for i in range(M):
        if t % time[i] == 0:
            cnt += 1
        if cnt == N:
            print(i + 1)
            break