from typing import List


class Solution:
    # 풀이 1. 분할 정복을 이용한 다양한 조합
    def diffWaysToCompute(self, expression: str) -> List[int]:
        def compute(left, right, op):
            results = []
            for l in left:
                for r in right:
                    results.append(eval(f"{l}{op}{r}"))
            return results

        if expression.isdigit():
            return [int(expression)]

        results = []
        for index, value in enumerate(expression):
            if value in '-+*':
                left = self.diffWaysToCompute(expression[:index])
                right = self.diffWaysToCompute(expression[index + 1:])

                results.extend(compute(left, right, value))
        return results


if __name__ == '__main__':
    solution = Solution()
    expression = "2*3-4*5"
    print(solution.diffWaysToCompute(expression))
