def solution(p):
    answer = ''
    if len(p) == 0:
        return answer
    else:
        normal = True
        open_count = 0
        close_count = 0
        cut_point = 0
        for i in range(len(p)):
            if p[i] == '(':
                open_count += 1
            else:
                close_count += 1

            if open_count - close_count < 0:
                normal = False

            if open_count == close_count:
                cut_point = i + 1
                break
        returned_p = solution(p[cut_point:])
        if normal:
            return p[:cut_point] + returned_p
        else:
            temp = ''
            for j in range(1, cut_point - 1):
                if p[j] == '(':
                    temp = temp + ')'
                else:
                    temp = temp + '('
            return '(' + returned_p + ')' + temp
