
testcase = 10

def dfs(v, end, N, path_list):                      # v에서 end에 도달하는지 확인하는 함수
    visited = [0] * N                               # 문제에서 노드 번호가 곧 인덱스번호라 하였으니 그대로 N개를 만들면 된다ㅓ
    stack = [0] * N
    top = -1

    visited[v] = 1                                  # 시작점 방문 표시

    while(True):
        for w in path_list[v]:
            if visited[w] == 0:
                top += 1
                stack[top] = v
                v = w
                visited[w] = 1
                break
        else:
            if top != -1:
                v = stack[top]
                top -= 1
            else:
                break
    if visited[end] == 1:                               # 방문했으면 True를 반환
        return True
    else:
        return False

for tc in range(1, testcase + 1):
    test_num, E = map(int, input().split())

    path_list = [[] for i in range(100)]                # 노드 수 만큼 리스트를 포함시키는 2차원 리스트

    paths = list(map(int, input().split()))             # 간선들이 일렬로 입력되므로 이를 시작 노드와 도착 노드로 구별해줘야한다
    for i in range(len(paths)):
        if i % 2 == 0:
            start = paths[i]
        else:
            end = paths[i]
            path_list[start].append(end)                # 노드번호가 곧 인덱스이므로 시작 노드 번호를 인덱스로 가지는 리스트에 삽입


    if dfs(0, 99, 100, path_list):
        print(f"#{tc} 1")
    else:
        print(f"#{tc} 0")
