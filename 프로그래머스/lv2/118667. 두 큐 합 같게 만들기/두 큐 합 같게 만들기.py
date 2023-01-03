from collections import deque

def solution(queue1, queue2):
    queue1, queue2 = deque(queue1), deque(queue2)

    count = 0
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    total_sum = sum1 + sum2
    max_len = len(queue1) * 3
    if total_sum % 2:
        return -1
    elif sum1 == sum2:
        return 0
    else:
        while sum1 != sum2:
            if sum1 > sum2:
                temp = queue1.popleft()
                queue2.append(temp)
                sum1 -= temp
                sum2 += temp
                count += 1
            else:
                temp = queue2.popleft()
                queue1.append(temp)
                sum2 -= temp
                sum1 += temp
                count += 1

            if count > max_len:
                return -1

        return count
