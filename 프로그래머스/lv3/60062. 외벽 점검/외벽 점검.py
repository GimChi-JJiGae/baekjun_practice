import itertools

def solution(n, weak, dist):
    answer = len(dist) + 1
    length = len(weak)
    
    for i in range(length):
        weak.append(weak[i] + n)
        
    for perm in itertools.permutations(dist, len(dist)):
        for start in range(length):
            count = 1
            position = weak[start] + perm[count-1]
            
            for i in range(start, start + length):
                if position < weak[i]:
                    count += 1
                    if count > len(dist):
                        break
                    position = weak[i] + perm[count-1]
            
            answer = min(answer, count)
            
    if answer > len(dist):
        return -1
    
    return answer