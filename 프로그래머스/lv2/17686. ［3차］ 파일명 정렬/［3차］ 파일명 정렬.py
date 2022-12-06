def solution(files):
    head_dict = {}
    answer = []
    for i in range(len(files)):
        head_name = ""
        number_name = ""
        number_start = 0
        tail_start = 0
        for j in range(len(files[i])):
            if files[i][j].isnumeric():
                number_start = j
                break
            head_name = head_name + files[i][j]

        for j in range(number_start, len(files[i])):
            if not files[i][j].isnumeric():
                tail_start = j
                break
            number_name = number_name + files[i][j]


        try:
            check = head_dict[head_name.upper()]
            head_dict[head_name.upper()].append([int(number_name), i])

        except KeyError:
            head_dict[head_name.upper()] = [[int(number_name), i]]


    # key list를 뽑아서 키 안의 값들을 numbername 별로 정리하자, 만약 같을 경우 들어온 순서니까 조심
    # 이후 key list를 소팅한 후 소팅된 키리스 안의 값들을 하나씩 집어넣으면 됨
    name_key_list = list(head_dict.keys())
    name_key_list.sort()
    for i in range(len(name_key_list)):
        head_dict[name_key_list[i]].sort(key=lambda x:x[0])
        for j in range(len(head_dict[name_key_list[i]])):
            answer.append(files[head_dict[name_key_list[i]][j][1]])


    return answer