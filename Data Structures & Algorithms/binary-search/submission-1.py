class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

            print(f"low={low}, high={high}, mid={mid}")

            value = nums[mid]

            if value < target:
                low = mid + 1
            elif value > target:
                high = mid - 1
            else:
                return mid

        return -1
