def solution(triangle):
    answer = 0

    for row in range(len(triangle)):
        if row == 0:
            continue
        for col in range(len(triangle[row])):
            if col == 0:
                triangle[row][col] += triangle[row - 1][col]
            elif col == len(triangle[row]) - 1:
                triangle[row][col] += triangle[row - 1][col - 1]
            else:
                if triangle[row - 1][col - 1] >= triangle[row - 1][col]:
                    triangle[row][col] += triangle[row - 1][col - 1]
                else:
                    triangle[row][col] += triangle[row - 1][col]

    answer = max(triangle[len(triangle)-1])
    return answer
