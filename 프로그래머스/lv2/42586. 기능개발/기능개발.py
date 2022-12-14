def solution(progresses, speeds):
    answer = []
    days = []
    for i in range(len(progresses)):
        tmp = 100-progresses[i]
        if tmp % speeds[i] == 0:
            days.append(tmp // speeds[i])
        else:
            days.append((tmp // speeds[i]) + 1)

    present_val = 0
    temp_val = 0
    for i in range(len(days)):
        if present_val < days[i]:
            answer.append(temp_val)
            present_val = days[i]
            temp_val = 1
        else:
            temp_val += 1
    else:
        answer.append(temp_val)
    answer.pop(0)
    return answer