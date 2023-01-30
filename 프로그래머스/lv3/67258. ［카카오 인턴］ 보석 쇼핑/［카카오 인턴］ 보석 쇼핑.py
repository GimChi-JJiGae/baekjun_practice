
def solution(gems):
    target = len(set(gems))
    total_len = len(gems)
    start = 0
    end = 0
    gem_kind_dict = {gems[0] : 1}
    answer = [0, 0]
    shortest = len(gems)
    while(start <= end):
        if len(gem_kind_dict) == target:

            if end - start < shortest:
                answer[0] = start + 1
                answer[1] = end + 1
                shortest = end - start
        # print("---------")
        # print(start, end)
        # print(gem_kind_dict)
        # print(len(gem_kind_dict))

        if len(gem_kind_dict) < target:
            end += 1
            if end >= len(gems):
                break

            try:
                gem_kind_dict[gems[end]] += 1

            except KeyError:
                gem_kind_dict[gems[end]] = 1

        else:



            try:
                if gem_kind_dict[gems[start]] > 1:
                    gem_kind_dict[gems[start]] -= 1
                else:
                    gem_kind_dict.pop(gems[start])
                start += 1
            except KeyError:
                print("키에러 발생, 사실상 와서는 안되는 곳")




    return answer