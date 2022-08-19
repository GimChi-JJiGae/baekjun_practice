
testcase = int(input())

for tc in range(1, testcase + 1):
    blank_list = list(input())


    for i in range(len(blank_list)):
        if blank_list[i] == "(" and blank_list[i + 1] == ")":   # 레이저 위치를 찾는다
            blank_list[i] = "r_o"                               # raser_open
            blank_list[i + 1] = "r_c"                           # raser_close
            

    bar_num = blank_list.count("(")
    result = bar_num
    count = 0
    for i in range(len(blank_list)):
        if blank_list[i] == "(":
            count += 1
        elif blank_list[i] == ")":
            count -= 1
        elif blank_list[i] == "r_o":
            result += count

    print(f"#{tc} {result}")



