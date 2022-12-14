def solution(s):
    answer = True
    open_count = 0
    close_count = 0

    for i in range(len(s)):
        if s[i] == '(':
            open_count += 1
        else:
            close_count += 1
        if open_count - close_count < 0:
            answer = False
            break
    else:
        if open_count != close_count:
            answer = False
    
    return answer