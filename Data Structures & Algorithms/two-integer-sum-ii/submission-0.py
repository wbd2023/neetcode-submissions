class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        print(numbers)
        print(target)

        left, right = 0, len(numbers) - 1
        while numbers[left] + numbers[right] != target:
            print(left, right)

            if numbers[left] + numbers[right] < target:
                left += 1
            elif numbers[left] + numbers[right] > target:
                right -= 1

        return [left + 1, right + 1]  # 0-indexed to 1-indexed.
