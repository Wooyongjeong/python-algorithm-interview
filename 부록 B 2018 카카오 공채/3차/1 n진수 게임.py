def solution(n, t, m, p):
    def convert(num, base):
        arr = "0123456789ABCDEF"
        q, r = divmod(num, base)
        if q == 0:
            return arr[r]
        return convert(q, base) + arr[r]

    numbers = []
    for i in range(t * m):
        converted = convert(i, n)
        numbers.extend(converted)

    return ''.join([numbers[i] for i in range(p - 1, t * m, m)])


if __name__ == '__main__':
    print(solution(16, 16, 2, 1))
