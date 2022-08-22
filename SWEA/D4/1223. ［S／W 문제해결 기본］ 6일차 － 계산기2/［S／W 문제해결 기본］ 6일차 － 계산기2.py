
testcase = 10

for tc in range(1, testcase + 1):
    len_calc = int(input())
    tokens =list(map(str,input().rstrip()))     # 입력받기
    lst = []                                    # 빈 리스트 생성
    stack = []                                  # 스택 생성
    prior = {'*':2, '+':1}                      # 우선순위 설정
    for n in range(len(tokens)):                # 토큰의 길이만큼 반복하여
        if tokens[n].isdigit():                 # 만약 숫자이면 바로 lst에 추가
            lst.append(int(tokens[n]))

        else:                                   # 그외에 경우 tokens[n]이 stack[-1]의 우선순위와 같거나 보다 작으면 tokens[n]의 우선순위가 더 커질때까지 pop
            while stack and prior[tokens[n]] <= prior[stack[-1]]:
                lst.append(stack.pop())         # pop한것들은 lst에 추가 시켜줌
            stack.append(tokens[n])             # 위의 조건이 완료 되면 stack에 추가

    while len(stack) != 0:                      # stack에 남아있는 연산자들 lst에 추가
        lst.append(stack.pop())

    calc_list = []
    num_list = []

    idx = 0


    while(idx < len(lst)):

        if lst[idx] == "*":                     # * 연산자가 나오면 앞의 저장된 num_list 가장 뒤의 두 숫자를 곱함 
            a = num_list.pop()
            b = num_list.pop()
            num_list.append(a * b)

        elif lst[idx] == "+":                   # + 연산자가 나오면 앞의 저장된 num_list 가장 뒤의 두 숫자를 더함
            a = num_list.pop()
            b = num_list.pop()
            num_list.append(a + b)
        else:
            num_list.append(lst[idx])           # 숫자가 나올경우 그대로 num_list에 push

        idx += 1

    print(f"#{tc} {num_list[0]}")