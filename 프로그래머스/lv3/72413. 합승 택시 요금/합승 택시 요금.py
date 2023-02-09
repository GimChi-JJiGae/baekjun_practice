from math import inf


def solution(n, s, a, b, fares):
    # 0부터 시작하는 인덱스
    s, a, b = s - 1, a - 1, b - 1

    # inf 로 초기화된 거리행렬
    # 자기 자신으로 가는 간선 가중치는 0
    graph = [[inf] * n for _ in range(n)]
    for i in range(n):
        graph[i][i] = 0     

    # 거리행렬에 주어진 비용 넣기
    for fare in fares:
        u, v, w = fare
        graph[u - 1][v - 1] = graph[v - 1][u - 1] = w

    # 플로이드-와샬
    for k in range(n):          # 1. 모든 노드를 중간점(경로)으로 가정하면서
        for i in range(n):      # 2. 거리행렬을 순회
            for j in range(n):  # 3. 현재 거리행렬에 저장된 거리가 k를 거쳐가는 거리보다 멀면 갱신
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]
                # graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j]) 시간 거의 두 배 걸림..

    # 출발점을 기준으로 어떤 지점 k를 거쳐 각각 a와 b로 가는 최소 비용을 탐색
    ans = inf
    for k in range(n):
        ans = min(ans, graph[s][k] + graph[k][a] + graph[k][b])

    return ans