
testcase = 10

for tc in range(1, testcase + 1):
    a = int(input())                            # 필요없는 입력값
    N = 16
    matrix = [[] for i in range(N)]

    for i in range(N):
        matrix[i] = matrix[i] + list(input())
    # 갈림길 만을 스택에 넣어보자
    # 1: 상, 2: 우, 3: 하, 4: 좌
    route = []
    start_x = 0
    start_y = 0
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == "2":
                start_x = i
                start_y = j
                break

    while(True):
        if matrix[start_x][start_y] == "3":
            print(f"#{tc} 1")
            break
        matrix[start_x][start_y] = "1"
        temp = []
        temp.append(start_x)                    # 현재 위치 저장
        temp.append(start_y)
        if start_x - 1 >= 0:
            if matrix[start_x - 1][start_y] == "0" or matrix[start_x - 1][start_y] == "3":     # 주변에 0이나 3이 있어 이동가능한지 확인
                temp.append(1)
        if start_y + 1 < N:
            if matrix[start_x][start_y + 1] == "0" or matrix[start_x][start_y + 1] == "3":
                temp.append(2)
        if start_x + 1 < N:
            if matrix[start_x + 1][start_y] == "0" or matrix[start_x + 1][start_y] == "3":
                temp.append(3)
        if start_y - 1 >= 0:
            if matrix[start_x][start_y - 1] == "0" or matrix[start_x][start_y - 1] == "3":
                temp.append(4)

        if len(temp) == 2:                                            # 막다른 길일 때, 갈림길로 돌아간다.

            if len(route) == 0:                                       # 돌아갈 갈림길이 없는데 길도 없어...
                print(f"#{tc} 0")
                break

            while(len(route[-1]) == 2):                               # 다른 갈림길이 남아 있던 곳까지 다시 이동
                route.pop()
                if len(route) == 0:                                   # pop하면서 찾아보았는데 없어서 모두 pop되버린 경우
                    break
            if len(route) == 0:                                       # 돌아갈 갈림길이 없는데 길도 없어...
                print(f"#{tc} 0")
                break
            else:
                start_x = route[-1][0]
                start_y = route[-1][1]
                route.pop()                                           # 다시 이 구간을 조사할 때 route 추가할거니까, 그 때는 확인했던 길은 1로 막혀있다

        elif len(temp) == 3:                                          # 갈 수 있는 길이 하나 뿐일 때는 그 길로 가면된다
            if temp[2] == 1:
                start_x = start_x - 1
                continue
            elif temp[2] == 2:
                start_y = start_y + 1
                continue
            elif temp[2] == 3:
                start_x = start_x + 1
                continue
            elif temp[2] == 4:
                start_y = start_y - 1
                continue

        elif len(temp) > 3:                                           # 여러갈래로 갈 수 있을 때, temp에 가장 마지막으로 입력된 방향으로 먼저가자
            route.append(temp)
            if route[-1][-1] == 1:
                start_x = start_x - 1
                continue
            elif route[-1][-1] == 2:
                start_y = start_y + 1
                continue
            elif route[-1][-1] == 3:
                start_x = start_x + 1
                continue
            elif route[-1][-1] == 4:
                start_y = start_y - 1
                continue
