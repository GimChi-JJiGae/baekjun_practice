import copy

def solution(key, lock):
    answer = False
    n = len(key)
    m = len(lock)

    # key2 = [[0 for _ in range(n)] for __ in range(n)]
    # key3 = [[0 for _ in range(n)] for __ in range(n)]
    # key4 = [[0 for _ in range(n)] for __ in range(n)]

    # 4가지 방향으로 확인하자

    key1 = []
    key2 = []
    key3 = []
    key4 = []

    holes = []

    for i in range(m):
        for j in range(m):
            if lock[i][j] == 0:
                holes.append((i, j))
    #
     #             key2[j][n - i - 1] = 1
    #             key3[n - i - 1][n - j - 1] = 1
    #             key4[n - j - 1][1] = 1

    for i in range(n):
        for j in range(n):
            if key[i][j] == 1:
                key1.append([i - n,j - n])
                key2.append([j - n, n - i - 1 - n])
                key3.append([n - i - 1 - n , n - j - 1 - n])
                key4.append([n - j - 1 - n , i - n])
            # n만큼 더 뺴줘서 키의 오른쪽 아래부터 차례로 확인하고자 하기 위함

    holes = set(tuple(holes))
    # key1 = set(key1)
    # key2 = set(key2)
    # key3 = set(key3)
    # key4 = set(key4)

    for i in range(n + m):
        for j in range(n + m):
            temp1 = copy.deepcopy(key1)
            temp2 = copy.deepcopy(key2)
            temp3 = copy.deepcopy(key3)
            temp4 = copy.deepcopy(key4)


            for k in range(len(key1)):


                temp1[k][0] = temp1[k][0] + i
                temp2[k][0] = temp2[k][0] + i
                temp3[k][0] = temp3[k][0] + i
                temp4[k][0] = temp4[k][0] + i

                temp1[k][1] = temp1[k][1] + j
                temp2[k][1] = temp2[k][1] + j
                temp3[k][1] = temp3[k][1] + j
                temp4[k][1] = temp4[k][1] + j

                temp1[k] = tuple(temp1[k])
                temp2[k] = tuple(temp2[k])
                temp3[k] = tuple(temp3[k])
                temp4[k] = tuple(temp4[k])

            temp1 = tuple(temp1)
            temp2 = tuple(temp2)
            temp3 = tuple(temp3)
            temp4 = tuple(temp4)

            if set(temp1) >= holes:
                temp1_list = list(set(temp1) - holes)
                for l in range(len(temp1_list)):
                    if 0 <= temp1_list[l][0] < m:
                        if 0 <= temp1_list[l][1] < m:
                            break
                else:
                    return True

            if set(temp2) >= holes:
                temp2_list = list(set(temp2) - holes)
                for l in range(len(temp2_list)):
                    if 0 <= temp2_list[l][0] < m:
                        if 0 <= temp2_list[l][1] < m:
                            break
                else:
                    return True

            if set(temp3) >= holes:
                temp3_list = list(set(temp3) - holes)
                for l in range(len(temp3_list)):
                    if 0 <= temp3_list[l][0] < m:
                        if 0 <= temp3_list[l][1] < m:
                            break
                else:
                    return True

            if set(temp4) >= holes:
                temp4_list = list(set(temp4) - holes)
                for l in range(len(temp4_list)):
                    if 0 <= temp4_list[l][0] < m:
                        if 0 <= temp4_list[l][1] < m:
                            break
                else:
                    return True


    return answer