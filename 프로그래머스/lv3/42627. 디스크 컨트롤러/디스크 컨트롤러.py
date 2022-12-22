def solution(jobs):
    total_time = 0
    now = 0
    total_jobs = len(jobs)
    jobs = sorted(jobs, key=lambda x: x[1])  # 빨리끝나는 것부터 처리하자

    while len(jobs) > 0:
        for i in range(len(jobs)):
            if jobs[i][0] <= now:            # 남아있는 것 중 시작할 수 있는것이라면
                now += jobs[i][1]
                total_time += now - jobs[i][0]
                jobs.pop(i)
                break

            if i == len(jobs) - 1:
                now += 1

    return total_time // total_jobs