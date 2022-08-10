N = int(input())
num_list = list(map(int, input().split()))

length = 1                                      # 얼마나 이어지고 있는가를 확인
max_length = 0
same_length = 0                                 # 같은 것이 연속으로 나온 길이
up_t_down_f = True                              # 오름차순이면 True, 내림차순이면 False를 가지는 변수이다.
if N == 1:
    max_length = 1
for i in range(N - 1):
    if i == 0:

        if num_list[i] > num_list[i + 1]:
            up_t_down_f = False
            length += 1
        elif num_list[i] < num_list[i + 1]:
            up_t_down_f = True
            length += 1
        else:
            same_length += 1
            length += 1
    else:
        if up_t_down_f:
            if num_list[i] < num_list[i + 1]:
                length += 1
                if same_length != 0:

                    same_length = 0
            elif num_list[i] > num_list[i + 1]:
                length = 2
                up_t_down_f = False
                if same_length != 0:
                    length += same_length
                    same_length = 0
            else:
                length += 1
                same_length += 1

        else:
            if num_list[i] > num_list[i + 1]:
                length += 1
                if same_length != 0:

                    same_length = 0
            elif num_list[i] < num_list[i + 1]:
                length = 2
                up_t_down_f = True
                if same_length != 0:
                    length += same_length
                    same_length = 0
            else:
                length += 1
                same_length += 1
    if length > max_length:
        max_length = length
print(max_length)


