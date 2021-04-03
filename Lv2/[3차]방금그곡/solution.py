def make_music(start, end, name, music):
    start_time = start.split(':')
    end_time = end.split(':')

    h_time = 0
    m_time = 0

    if int(start_time[0]) <= int(end_time[0]):
        h_time = int(end_time[0]) - int(start_time[0])
    else:
        h_time = 24 - int(start_time[0]) + int(end_time[0])

    if int(start_time[1]) <= int(end_time[1]):
        m_time = int(end_time[1]) - int(start_time[1])
    else:
        m_time = 60 - int(start_time[1]) + int(end_time[1])
        h_time -= 1

    total_time = 60 * h_time + m_time
    tmp_total_time = total_time
    total_music = ''
    idx = 0

    while tmp_total_time > 0:

        total_music += music[idx]
        idx = (idx + 1) % len(music)

        if music[idx] == '#':
            total_music += '#'
            idx = (idx + 1) % len(music)

        tmp_total_time -= 1

    return total_time, total_music


def to_folmula(musicinfos):
    musicinfo = []
    for data in musicinfos:
        now = data.split(',')
        start_time = now[0]
        end_time = now[1]
        name = now[2]
        music = now[3]
        musicinfo.append([start_time, end_time, name, music])
    return musicinfo


def check(lyb, m):
    if len(m) > len(lyb):
        return False
    for i in range(len(lyb) - len(m) + 1):
        if lyb[i:i + len(m)] == m:
            if i + len(m) < len(lyb) and lyb[i + len(m)] == '#':
                continue
            else:
                return True


def solution(m, musicinfos):
    answer = ''
    max_time = 0
    musicinfo = to_folmula(musicinfos)

    for i in range(len(musicinfos)):
        time, lyb = make_music(musicinfo[i][0], musicinfo[i][1], musicinfo[i][2], musicinfo[i][3])
        print(lyb)
        if check(lyb, m) and max_time < time:
            answer = musicinfo[i][2]
            max_time = time

    if answer == '':
        return '(None)'
    return answer