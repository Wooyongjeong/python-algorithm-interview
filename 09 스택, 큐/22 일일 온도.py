# 풀이 1. 스택 값 비교
def dailyTemperatures1(temperatures: list[int]) -> list[int]:
    answer = [0] * len(temperatures)
    stack = []
    for i, cur in enumerate(temperatures):
        # 현재 온도가 스택 값보다 높다면 정답 처리
        while stack and cur > temperatures[stack[-1]]:
            last = stack.pop()
            answer[last] = i - last
        stack.append(i)

    return answer


if __name__ == '__main__':
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    print(dailyTemperatures1(temperatures))
