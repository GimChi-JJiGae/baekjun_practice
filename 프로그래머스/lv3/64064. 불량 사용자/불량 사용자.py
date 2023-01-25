def pick(sample_list, idx, result_list, last):
    if len(result_list) == last:
        return [result_list]
    temp_result = []
    for i in range(len(sample_list[idx])):
        temp = result_list[:]
        if sample_list[idx][i] in temp:
            continue
        temp.append(sample_list[idx][i])
        temp_result.extend(pick(sample_list, idx + 1, temp, last))
    return temp_result

def solution(user_id, banned_id):

    banned_pos_list = []

    for i in range(len(banned_id)):

        banned_pos_list.append([])
        for j in range(len(user_id)):
            if len(banned_id[i]) != len(user_id[j]):    # 길이가 다르면 해당사항 없음
                continue
            else:
                for k in range(len(banned_id[i])):
                    if banned_id[i][k] == "*":
                        continue
                    if banned_id[i][k] != user_id[j][k]:
                        break
                else:
                    banned_pos_list[i].append(j)     # 가능한 아이디면 그 인덱스를 넣어두자

    print(banned_pos_list)
    anwer_list = []
    result_list = pick(banned_pos_list, 0, [], len(banned_pos_list))
    for i in range(len(result_list)):
        tmp = set(result_list[i])
        # if len(tmp) != len(banned_pos_list):
        #     continue
        # else:
        if tmp not in anwer_list:
            anwer_list.append(tmp)
    answer = len(anwer_list)
    return answer