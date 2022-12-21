def solution(m, musicinfos):
    answer = '(None)'
    m = m.replace('A#', 'H')
    m = m.replace('C#', 'I')
    m = m.replace('D#', 'J')
    m = m.replace('F#', 'K')
    m = m.replace('G#', 'L')
    longest_time = 0
    for i in range(len(musicinfos)):
        infos = list(musicinfos[i].split(','))
        infos[3] = infos[3].replace('A#', 'H')
        infos[3] = infos[3].replace('C#', 'I')
        infos[3] = infos[3].replace('D#', 'J')
        infos[3] = infos[3].replace('F#', 'K')
        infos[3] = infos[3].replace('G#', 'L')
        start_time = int(infos[0][:2]) * 60 + int(infos[0][3:])
        end_time = int(infos[1][:2]) * 60 + int(infos[1][3:])
        song_length = len(infos[3])
        total_time = end_time - start_time
        t = total_time // song_length
        l = total_time % song_length

        melody = ''
        for j in range(t):
            melody = melody + infos[3]
        melody = melody + infos[3][:l]

        if m in melody:
            if longest_time < total_time:
                longest_time = total_time
                answer = infos[2]

    return answer