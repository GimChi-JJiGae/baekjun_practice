def solution(clothes):
    answer = 0
    clothes_dict = {}

    for i in range(len(clothes)):
        try:
            clothes_dict[clothes[i][1]] += 1
        except KeyError:
            clothes_dict[clothes[i][1]] = 1
    dict_key_list = list(clothes_dict.keys())
    print(clothes_dict)
    tmp = 1
    for i in range(len(dict_key_list)):
        tmp = tmp * (clothes_dict[dict_key_list[i]] + 1)
    answer += tmp

    answer -= 1
    return answer
