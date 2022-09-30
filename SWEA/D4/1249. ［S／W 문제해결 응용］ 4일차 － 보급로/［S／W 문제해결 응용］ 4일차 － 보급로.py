from heapq import heappush
from heapq import heappop

testcase = int(input())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for tc in range(1, testcase + 1):
    N = int(input())
    matrix = []
    visited = []
    for i in range(N):
        matrix.append(list((input())))
        visited.append([1000*N*N*10 for _ in range(N)])

    visited[0][0] = 0

    heap =[]
    heappush(heap, [0, [0, 0]])          # 값이 두개들어있는 리스트들이 들어있음, 0번은 거리, 1번 인덱스는 위치

    while(heap):

        temp = heappop(heap)
        idx_i = temp[1][0]
        idx_j = temp[1][1]

        for i in range(4):
            if 0 <= idx_i+dx[i] < N and 0 <= idx_j+dy[i] < N:
                if visited[idx_i+dx[i]][idx_j+dy[i]] > visited[idx_i][idx_j] + int(matrix[idx_i+dx[i]][idx_j+dy[i]]):
                    visited[idx_i+dx[i]][idx_j+dy[i]] = visited[idx_i][idx_j] + int(matrix[idx_i+dx[i]][idx_j+dy[i]])
                    heappush(heap, [visited[idx_i + dx[i]][idx_j + dy[i]], [idx_i + dx[i], idx_j + dy[i]]])

            else:
                continue

    print(f"#{tc} {visited[N-1][N-1]}")
