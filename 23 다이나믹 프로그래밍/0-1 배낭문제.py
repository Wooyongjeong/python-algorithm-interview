def zero_one_knapsack(cargo):
    capacity = 15
    pack = []

    for i in range(len(cargo) + 1):
        # pack[i][j]: 물건 i까지 넣을 수 있고, 가방의 최대 무게가 j일 때의 물건 가치의 총합의 최댓값
        pack.append([])
        for c in range(capacity + 1):
            if i == 0 or c == 0:
                pack[i].append(0)
            elif cargo[i - 1][1] <= c:
                pack[i].append(
                    max(
                        # i번째 물건을 넣었을 때
                        # (i번째 물건의 가치) + (i번째 물건의 무게만큼 안 넣었을 때 가치 최댓값)
                        cargo[i - 1][0] + pack[i - 1][c - cargo[i - 1][1]],
                        # i번째 물건을 넣지 않았을 때 비교
                        pack[i - 1][c]
                    ))
            else:
                pack[i].append(pack[i - 1][c])
    return pack[-1][-1]


if __name__ == '__main__':
    # (가격, 무게)
    cargo = [
        (4, 12),
        (2, 1),
        (10, 4),
        (1, 1),
        (2, 2),
    ]
    r = zero_one_knapsack(cargo)
    print(r)
