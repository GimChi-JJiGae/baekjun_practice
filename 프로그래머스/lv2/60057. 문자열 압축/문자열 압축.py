def solution(s):
    min_len = len(s)
    total = ""
    for i in range(1, len(s)):
        word = s[:i]
        len_word = len(word)
        count = 1
        skip = 0
        for j in range(i, len(s)):
            if skip:
                skip -= 1
                continue
            if s[j:j+len_word] == word:
                count += 1
                skip = len_word - 1
                continue
            else:
                if count > 1:
                    total = total + str(count) + word
                else:
                    total = total + word
                word = s[j:j+i]
                count = 1
                skip = len_word - 1

        else:
            if count > 1:
                total = total + str(count) + word
            else:
                total = total + word

            if len(total) < min_len:
                min_len = len(total)
            total = ""
    return min_len