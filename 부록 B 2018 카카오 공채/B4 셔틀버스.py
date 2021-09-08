# 입력값 전처리 및 대기 시각 처리
def solution(n, t, m, timetable):
    # 입력값 분 단위 전처리
    timetable = [
        int(time[:2]) * 60 + int(time[3:])
        for time in timetable
    ]
    timetable.sort()

    current = 9 * 60
    # 셔틀 운행 횟수 n에 따라 대기자가 m만큼 탑승할 수 있도록 구현
    for _ in range(n):
        for _ in range(m):
            # 1. 먼저 온 사람이 먼저 탑승
            # 버스 출발 시각보다 먼저 온 사람 -> 큐 연산을 통해 항상 탑승
            # 이 경우 콘이 먼저 타야하므로 콘은 1분 먼저 타도록 설정
            if timetable and timetable[-1] <= current:
                candidate = timetable.pop() - 1
            # 2. 더 이상 탈 사람이 없음
            # 최대한 늦게 오는 것이 목표 -> 현재 버스가 온 시각으로 설정
            else:
                candidate = current
        # 셔틀 운행 간격 t
        current += t

    h, m = divmod(candidate)
    return f"{str(h).zfill(2)}:{str(m).zfill(2)}"
