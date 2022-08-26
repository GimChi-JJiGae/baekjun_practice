
testcase = 10

for tc in range(1, testcase + 1):
    num = int(input())                                      # 사용하지 않을 값

    ladder = [[] for i in range(100)]
    for i in range(100):
        ladder[i] = ladder[i] + list(map(int, input().split()))

    counting_dict = {}
    where_ = {}
    for i in range(100):                                    # 출발 지점 확인
        if ladder[0][i] == 1:
            counting_dict[i] = 0
            where_[i] = i                                   # 현재 위치에 어떤 출발 인덱스값이 들어있는지 확인하는 딕셔너리

    starts = list(counting_dict.keys())
    num_of_start = len(starts)
    # 어차피 다 내려가야하니까 내려가는 길이는 굳이 더해주지 말자, 양옆으로 움직이는 길이만 확인
    for i in range(100):

        for j in range(num_of_start - 1):                   # 가장 오른쪽을 제외한 나머지 내려가는 길만 확인
            if ladder[i][starts[j] + 1] == 1:               # 오른쪽으로 가는 다리가 있는지 확인
                distance = starts[j + 1] - starts[j]        # 다리가 있다면 그 거리는 이와 같다
                counting_dict[where_[starts[j]]] = counting_dict[where_[starts[j]]] + distance          # 두 내려가는 길에 거리만큼 더해줌
                counting_dict[where_[starts[j + 1]]] = counting_dict[where_[starts[j + 1]]] + distance  # 현재 위치에 들어있는 시작 인덱스를 알아낸 후 counting_dict의 key값으로 이용함

                temp = where_[starts[j + 1]]                                     # 두 개의 위치가 바뀌었으니 값을 바꿔준다.
                where_[starts[j + 1]] = where_[starts[j]]
                where_[starts[j]] = temp


    result = min(counting_dict, key=counting_dict.get)

    print(f"#{tc} {result}")



