testcase = int(input())


for tc in range(1, testcase + 1):
    N = int(input())
    matrix = []
    for i in range(N):
        matrix.append(list(map(int, input().split())))

    max_length = -1

    for i in range(N):
        for j in range(N):



            for k in range(1, min(i, N - (j + 1))+1):
                for l in range(1, min(N- (i + 1), (N - (j + k + 1)))+1):
                    way = []
                    new_i = i
                    new_j = j
                    way.append(matrix[new_i][new_j])
                    for a in range(1, k + 1):
                        new_i = new_i - 1
                        new_j = new_j + 1
                        way.append(matrix[new_i][new_j])
                    for b in range(1, l + 1):
                        new_i = new_i + 1
                        new_j = new_j + 1
                        way.append(matrix[new_i][new_j])
                    for c in range(1, k + 1):
                        new_i = new_i + 1
                        new_j = new_j - 1
                        way.append(matrix[new_i][new_j])
                    for d in range(1, l + 1):
                        new_i = new_i - 1
                        new_j = new_j - 1
                        way.append(matrix[new_i][new_j])
                    way.pop()                           # 첫 숫자 중복제거


                    len_a = len(way)
                    len_b = len(set(tuple(way)))
                    if len_a == len_b:
                        if max_length < len_a:
                            max_length = len_a
    print(f"#{tc} {max_length}")





