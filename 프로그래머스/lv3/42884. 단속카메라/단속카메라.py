def solution(routes):
    answer = 0
    camera = []
    routes.sort(key=lambda x:x[1])
    for i in range(len(routes)):
        check = False
        for j in range(len(camera)):
            if camera[j] > routes[i][1]:
                break
            if routes[i][0] <= camera[j] <= routes[i][1]:
                check = True
                break
        if check:
            continue
        else:
            camera.append(routes[i][1])
            answer += 1
    return answer