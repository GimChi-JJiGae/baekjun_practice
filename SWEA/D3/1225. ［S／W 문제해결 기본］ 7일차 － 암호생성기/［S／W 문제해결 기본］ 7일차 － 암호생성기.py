
for tc in range(1, 11):
    a = int(input())        # 쓰지않을 값
    num_list = list(map(int, input().split()))

    min_val = min(num_list)
    useless = (min_val // 15) - 1                       # 한 사이클 정도는 더 돌아주자
    if useless == - 1:
        useless = 0                                     # -1을 곱하지는 않도록 하자.
    for i in range(8):
        num_list[i] = num_list[i] - (15 * useless)
 
    done = False
    while(not done):
        for i in range(5):
            pop_num = num_list.pop(0)
            val = pop_num - (i + 1)
            if val <= 0:
                val = 0
                num_list.append(val)
                done = True
                break
            else:
                num_list.append(val)

    print(f"#{tc} ",end="")
    print(*num_list)

