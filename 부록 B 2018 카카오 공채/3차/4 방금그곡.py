def solution(m, musicinfos):
    def sharp_to_lower(sound):
        s = sound.replace('C#', 'c').replace('D#', 'd').replace('F#', 'd')\
            .replace('G#', 'g').replace('A#', 'a')
        return s

    answer = []
    m = sharp_to_lower(m)

    for i, musicinfo in enumerate(musicinfos):
        start, end, title, sound = musicinfo.split(',')
        start = int(start[:2]) * 60 + int(start[3:])
        end = int(end[:2]) * 60 + int(end[3:])
        playing_time = end - start
        sound = sharp_to_lower(sound)
        while playing_time > len(sound):
            sound += sound
        sound = sound[:playing_time]
        if m in sound:
            answer.append((playing_time, i, title))
    if not answer:
        return "(None)"
    answer.sort(key=lambda x: (-x[0], x[1]))
    return answer[0][-1]



if __name__ == '__main__':
    m_lst = ["ABCDEFG", "CC#BCC#BCC#BCC#B", "ABC"]
    musicinfos_lst = [
        ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"],
        ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"],
        ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]
    ]

    for m, musicinfos in zip(m_lst, musicinfos_lst):
        print(m, musicinfos)
        print(solution(m, musicinfos))
