def solution(n, t, m, timetable):
    answer = ''
    timetable.sort()

    bus_time = {}
    for i in range(n):
        bus_time[9*60 + t*i] = []

    key_list = list(bus_time.keys())

    for i in range(len(timetable)):


        if len(bus_time[key_list[-1]]) == m:
            break

        temp = timetable[i]
        hour = int(temp[:2]) * 60
        minute = int(temp[3:])
        time = hour + minute

        if key_list[-1] < time:
            break

        for j in range(len(key_list)):
            if key_list[j] < time:
                continue
            else:
                if len(bus_time[key_list[j]]) < m :
                    bus_time[key_list[j]].append(time)
                    break
                else:
                    continue

    if len(bus_time[key_list[-1]]) < m:
        hourstring = str(key_list[-1] // 60)
        minutestring = str(key_list[-1] % 60)
        if len(hourstring) == 1:
            hourstring = "0" + hourstring
        if len(minutestring) == 1:
            minutestring = "0" + minutestring
        answer = hourstring + ":" + minutestring
    else:
        hourstring = str((bus_time[key_list[-1]][-1] - 1) // 60)
        minutestring = str((bus_time[key_list[-1]][-1] - 1) % 60)
        if len(hourstring) == 1:
            hourstring = "0" + hourstring
        if len(minutestring) == 1:
            minutestring = "0" + minutestring
        answer = hourstring + ":" + minutestring
    print(bus_time)
    return answer