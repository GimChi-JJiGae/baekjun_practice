def cal_kevin_bacon (V_list, E_dict):
    min_val = len(V_list) * len(E_dict)
    In_SSA = V_list[0]
    for guy in V_list:
        visited = [0] * (len(V_list) + 1)         # 인덱스 에러 방지용 하나 추가

        q = []
        visited[guy] = 1
        q.append(guy)
        while(q):
            v = q.pop(0)
            for w in E_dict[v]:
                if visited[w] == 0:
                    q.append(w)
                    visited[w] = visited[v] + 1
                else:
                    continue
        local_sum = sum(visited)
        if local_sum < min_val:
            min_val = local_sum
            In_SSA = guy
    return In_SSA

V, E = map(int, input().split())

people = [i + 1 for i in range(V)]
edge_dict = {i + 1: [] for i in range(V)}

for i in range(E):
    a, b = map(int, input().split())
    edge_dict[a].append(b)
    edge_dict[b].append(a)

print(cal_kevin_bacon(people, edge_dict))

