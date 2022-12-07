from itertools import combinations

def solution(orders, course):

    answer = []
    for num_of_menu in course:
        maximum = 0
        counting_dict = {}
        mini_result = []
        for i in range(len(orders)):
            if len(orders[i]) >= num_of_menu:
                orders_list = list(orders[i])
                orders_list.sort()
                temp = list(combinations(orders_list, num_of_menu))

                for comb in temp:
                    tmp_str = ''.join(comb)

                    try:
                        check = counting_dict[tmp_str]

                    except KeyError:
                        counting_dict[tmp_str] = 0
                        temp_count = 0
                        for j in range(len(orders)):
                            for k in range(len(tmp_str)):
                                if tmp_str[k] not in orders[j]:
                                    break
                            else:
                                temp_count += 1

                            if temp_count + len(orders) - j - 1 < maximum:
                                break

                        else:
                            if temp_count < 2:
                                continue
                            if temp_count > maximum:
                                maximum = temp_count
                                mini_result.clear()
                                mini_result.append(tmp_str)

                            elif temp_count == maximum:
                                mini_result.append(tmp_str)
                            else:
                                print("오류")
        answer.extend(mini_result)
    answer.sort()
    return answer