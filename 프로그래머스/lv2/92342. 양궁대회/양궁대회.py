max_gap = -56
answers = []
count = 0

def ShootOrNot(info, history, index, arrow):

    global max_gap
    global answers
    global count
    if arrow == 0:
        if len(history) < 11:
            for i in range(11 - len(history)):
                history.append(0)
        sum_of_history_ap = 0
        sum_of_history_li = 0
        for i in range(11):
            if history[i]:
                sum_of_history_li += 10 - i
            else:
                if info[i]:
                    sum_of_history_ap += 10 - i
        gap = sum_of_history_li - sum_of_history_ap
        if gap >= max_gap:
            if gap > max_gap:
                answers.clear()
                count = 1
            else:
                count += 1
            answers.append(history)
            max_gap = gap
        return

    if index == 11:


        sum_of_history_ap = 0
        sum_of_history_li = 0
        if arrow:
            history[-1] = history[-1] + arrow

        for i in range(11):
            if history[i]:
                sum_of_history_li += 10 - i
            else:
                if info[i]:
                    sum_of_history_ap += 10 - i
        gap = sum_of_history_li - sum_of_history_ap
        if gap >= max_gap:
            if gap > max_gap:
                answers.clear()
                count = 0
            else:
                count += 1
            answers.append(history)
            max_gap = gap
        return


    if info[index] >= arrow:    # 여기 다 쏴봤자 안됨
        ShootOrNot(info, history + [0], index + 1, arrow)
    else:
        ShootOrNot(info, history + [0], index + 1, arrow)
        ShootOrNot(info, history + [info[index] + 1], index + 1, arrow - (info[index] + 1))



def solution(n, info):
    global max_gap
    global answers
    global count
    ShootOrNot(info, [], 0, n)
    if max_gap <= 0:
        answer = [-1]
    else:
        if count == 1:
            answer = answers[-1]
        else:
            result = [''] * count
            for j in range(10, -1, -1):
                for i in range(count):
                    result[i] = result[i] + str(answers[i][j])
            what_we_want = '0'
            what_we_want_idx = 0

            for i in range(count):
                if result[i] > what_we_want:
                    what_we_want = result[i]
                    what_we_want_idx = i
            answer = answers[what_we_want_idx]

    return answer