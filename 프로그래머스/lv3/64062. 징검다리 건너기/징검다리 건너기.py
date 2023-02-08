def solution(stones, k):
    start = 0
    end = 200000000
    lowest = end

    while(start <= end):
        mid = (start + end) // 2  # ~번째로 건너는 사람이라고 생각하자
        # print(mid)
        count = 0
        for i in range(len(stones)):
            if mid > stones[i]:
                count += 1
                if count == k:
                    break
            else:
                count = 0
        else:                       # 무사히 다 돈다면 좀 더 높혀봐도 된다.
            start = mid + 1
            continue
                                    # 무사히 다 못 도니까 낮추자.
        end = mid - 1
        if lowest > mid:
            lowest = mid
            continue

    return lowest - 1