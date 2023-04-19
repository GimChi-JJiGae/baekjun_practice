def solution(rows, columns, queries):
    matrix = [[i * columns + j + 1 for j in range(columns)] for i in range(rows)]
    min_list = []
    answer = []
    # for i in range(rows):
    #     print(matrix[i])
    # print("---------")
    for q in range(len(queries)):

        i_start = queries[q][0] - 1
        j_start = queries[q][1] - 1
        i_end = queries[q][2] - 1
        j_end = queries[q][3] - 1


        # 귀퉁이값은 미리 뽑아두자
        point_s_s = matrix[i_start][j_start]
        point_s_e = matrix[i_start][j_end]
        point_e_s = matrix[i_end][j_start]
        point_e_e = matrix[i_end][j_end]
        min_Val = min(point_s_s, point_e_s, point_e_e, point_s_e)

        #윗부분부터q
        for i in range(j_end - j_start):
            matrix[i_start][j_end - i] = matrix[i_start][j_end - i - 1]
            if matrix[i_start][j_end - i - 1] < min_Val:
                min_Val = matrix[i_start][j_end - i - 1]

        # 오른쪽
        for i in range(i_end - i_start - 1):
            matrix[i_end - i][j_end] = matrix[i_end - i - 1][j_end]
            if matrix[i_end - i - 1][j_end] < min_Val:
                min_Val = matrix[i_end - i - 1][j_end]
        matrix[i_start + 1][j_end] = point_s_e

        #아랫쪽
        for i in range(j_end - j_start - 1):
            matrix[i_end][j_start + i] = matrix[i_end][j_start + i + 1]
            if min_Val > matrix[i_end][j_start + i + 1]:
                min_Val = matrix[i_end][j_start + i + 1]

        matrix[i_end][j_end - 1] = point_e_e

        #왼쪽
        for i in range(i_end - i_start - 1):
            matrix[i_start + i][j_start] = matrix[i_start + i + 1][j_start]
            if min_Val > matrix[i_start + i + 1][j_start]:
                min_Val = matrix[i_start + i + 1][j_start]
        matrix[i_end - 1][j_start] = point_e_s
        answer.append(min_Val)

        # for i in range(rows):
        #     print(matrix[i])
        # print("---------")


    return answer