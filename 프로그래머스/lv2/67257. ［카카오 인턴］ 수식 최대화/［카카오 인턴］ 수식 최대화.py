import itertools


def solution(expression):
    exp_list = ['+', '-', '*']
    cal_list = list(itertools.permutations(exp_list, 3))
    original = []
    answer = 0
    temp = ''
    for i in range(len(expression)):
        if expression[i].isdigit():
            temp = temp + expression[i]
        else:
            original.append(int(temp))
            temp = ''
            original.append(expression[i])
    original.append(int(temp))
    for i in range(len(cal_list)):
        contents = original[:]
        for j in range(3):
            tmp = len(contents)
            k = 0
            while k < len(contents):
                if contents[k] == cal_list[i][j]:


                    if contents[k] == '+':
                        contents[k] = contents[k - 1] + contents[k + 1]
                    elif contents[k] == '*':
                        contents[k] = contents[k - 1] * contents[k + 1]
                    else:
                        contents[k] = contents[k - 1] - contents[k + 1]
                    contents.pop(k - 1)
                    contents.pop(k)
                    k -= 2

                k += 1
        if abs(contents[0]) > answer:
            answer = abs(contents[0])
    return answer