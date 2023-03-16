def solution(play_time, adv_time, logs):
    answer = ''
    start_time = 0
    end_time = int(adv_time[:2]) * 60 * 60 + int(adv_time[3:5]) * 60 + int(adv_time[6:])
    total_time = int(play_time[:2]) * 60 * 60 + int(play_time[3:5]) * 60 + int(play_time[6:])
    adv_long = end_time - start_time

    max_view = 0
    max_time = 0

    time_list = [0 for i in range(total_time + 1)]

    for i in range(len(logs)):
        # 시작 시간


        time_list[int(logs[i][:2]) * 60 * 60 + int(logs[i][3:5]) * 60 + int(logs[i][6:8])] += 1

        # 끝 시간

        time_list[int(logs[i][9:11]) * 60 * 60 + int(logs[i][12:14]) * 60 + int(logs[i][15:])] -= 1



    for i in range(1, len(time_list)):
        time_list[i] = time_list[i - 1] + time_list[i]  # 누적합 계산을 여기서 한다.

    for i in range(1, len(time_list)):
        time_list[i] = time_list[i - 1] + time_list[i]  # 누적합 계산을 여기서 한다.

    for i in range(total_time):
        if i >= adv_long:
            if max_view < time_list[i] - time_list[i - adv_long]:
                max_view = time_list[i] - time_list[i - adv_long]
                max_time = i - adv_long + 1
        else:
            if max_view < time_list[i]:
                max_view = time_list[i]
                max_time = i - adv_long + 1

    answer = answer + str(max_time // 3600) + ":"
    if len(answer) < 3:
        answer = "0" + answer
    if len(str((max_time % 3600) // 60)) > 1:
        answer = answer + str((max_time % 3600) // 60) + ":"
    else:
        answer = answer + "0" + str((max_time % 3600) // 60) + ":"


    if len(str(max_time % 60)) > 1:
        answer = answer + str(max_time % 60)
    else:
        answer = answer + "0" + str(max_time % 60)


    return answer