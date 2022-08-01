n = int(input())
result = 0
word_list =[]
for i in range(n):
    a = input()
    word_list.append(a)
for i in range(n): # 단어 수만큼 반복
    # 확인할 단어
    is_group = True # 그룹단어 표시를 위함
    check_list = [] # 나온 알파벳을 저장하기 위함
    idx = -1 # check_list의 체크 중인 index를 나타냄, 하나가 들어가면 0이되므로 -1
    word = word_list[i]
    for j in word:
        if j not in check_list:
            check_list.append(j)
            idx += 1
        else:
            if check_list[idx] == j: # 계속 반복중인 글자임
                continue
            else:
                is_group = False
                break
    if is_group:
        result += 1

print(result)
