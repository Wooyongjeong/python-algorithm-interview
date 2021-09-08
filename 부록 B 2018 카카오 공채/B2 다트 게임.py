# 문자열 및 자릿수 올림 처리
def solution(dartResult):
    answer = [0]
    sdt = list('SDT')
    for s in dartResult:
        if s in sdt:
            answer[-1] **= sdt.index(s) + 1
            answer.append(0)
        elif s == '*':
            answer[-2] *= 2
            if len(answer) > 2:
                answer[-3] *= 2
        elif s == '#':
            answer[-2] *= -1
        else:
            answer[-1] = answer[-1] * 10 + int(s)
    return sum(answer)


if __name__ == '__main__':
    dartResults = ['1S2D*3T', '1D2S#10S', '1D2S0T', '1S*2T*3S', '1D#2S*3S',
                   '1T2D3D#', '1D2S3T*']
    for dartResult in dartResults:
        print(dartResult, solution(dartResult))
