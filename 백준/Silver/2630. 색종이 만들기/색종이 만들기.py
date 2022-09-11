N = int(input())
matrix = []
for i in range(N):
    matrix.append(list(map(int, input().split())))

count_zero = 0
count_one = 0

def count_paper(n, start_i, start_j):

    global count_zero
    global count_one
    global matrix

    if n == 1:
        if matrix[start_i][start_j] == 0:
            count_zero += 1
            return
        else:
            count_one += 1
            return

    else:
        first = matrix[start_i][start_j]
        for i in range(start_i, start_i + n):
            for j in range(start_j, start_j + n):
                if first != matrix[i][j]:
                    count_paper(n // 2, start_i, start_j)
                    count_paper(n // 2, start_i, start_j + (n // 2))

                    count_paper(n // 2, start_i + (n // 2), start_j)
                    count_paper(n // 2, start_i + (n // 2), start_j + (n // 2))

                    return

        else:

            if first == 0:
                count_zero += 1
                return
            else:
                count_one += 1
                return

count_paper(N, 0, 0)

print(count_zero)
print(count_one)