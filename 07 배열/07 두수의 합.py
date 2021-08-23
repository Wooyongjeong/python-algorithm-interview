# 풀이 1. 브루트 포스로 계산
def twoSums(nums: list[int], target: int) -> list[int]:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


# 풀이 2. in을 이용한 탐색
def twoSums2(nums: list[int], target: int) -> list[int]:
    for i, n in enumerate(nums):
        complement = target - n

        if complement in nums[i + 1:]:
            return [nums.index(n), nums[i + 1:].index(complement) + (i + 1)]


# 풀이 3. 첫 번째 수를 뺀 결과 키 조회
def twoSums3(nums: list[int], target: int) -> list[int]:
    nums_map = {}
    # 키와 값을 바꿔서 딕셔너리로 저장
    for i, num in enumerate(nums):
        nums_map[num] = i

    # target에서 첫 번째 수를 뺀 결과를 키로 조회
    for i, num in enumerate(nums):
        if target - num in nums_map and i != nums_map[target - num]:
            return [i, nums_map[target - num]]


# 풀이 4. 조회 구조 개선
def twoSums4(nums: list[int], target: int) -> list[int]:
    nums_map = {}
    # 하나의 for문으로 통합
    for i, num in enumerate(nums):
        if target - num in nums_map:
            return [i, nums_map[target - num]]
        nums_map[num] = i


# 풀이 5. 투 포인터 이용
def twoSums5(nums: list[int], target: int) -> list[int]:
    left, right = 0, len(nums) - 1
    while not left == right:
        # 합이 target보다 작으면 left를 오른쪽으로
        if nums[left] + nums[right] < target:
            left += 1
        # 합이 target보다 크면 right를 왼쪽으로
        elif nums[left] + nums[right] > target:
            right -= 1
        else:
            return [left, right]
'''
그치만 이 문제에서는 투 포인터를 이용할 수 없음..
nums가 정렬된 상태가 아니기 때문에 위의 풀이가 적용되지 않음!
그럼 nums.sort()를 해야되는데, 그럼 index가 엉망이 됨!
코테에서 풀이를 잘못 택해서 이런 형태로 풀이를 진행했다면, 왜 안되는지 찾아내는데 좀 고생할 거임
오프라인 인터뷰라면 면접관이 지적해줄텐데... ㅠ
이런 부분에서 시간 허비하면 매우 큰 시간 낭비가 될 수 있으니 조심해야함!!
'''

# 풀이 5. 투 포인터로 풀어본 거
def two_sums(nums: list[int], target: int) -> list[int]:
    nums = [(num, i) for num, i in enumerate(nums)]
    nums.sort(key=lambda x: x[0])
    left, right = 0, len(nums) - 1
    while not left == right:
        left_value, right_value = nums[left][0], nums[right][0]
        # 합이 target보다 작다 -> 그럼 더 큰 수를 봐야함 -> left를 오른쪽으로
        if left_value + right_value < target:
            left += 1
        # 합이 target보다 크다 -> 그럼 더 작은 수를 -> right를 왼쪽으로
        elif left_value + right_value > target:
            right -= 1
        else:
            return [nums[left][1], nums[right][1]]


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    print(two_sums(nums, target))
