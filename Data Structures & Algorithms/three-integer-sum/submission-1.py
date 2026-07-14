class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []

        nums.sort()
        left, right = 0, len(nums) - 1

        print(nums)

        while left < right:
            complement = 0 - (nums[left] + nums[right])
            low, high = left, right

            # print(left, right)

            while low < high:
                mid = low + (high - low) // 2

                # print(mid)

                if nums[mid] < complement:
                    low = mid + 1
                elif nums[mid] > complement:
                    high = mid - 1
                else:
                    result = [nums[left], nums[mid], nums[right]]
                    if result not in results:
                        results.append(result)
                    break

            if complement < 0:
                right -= 1
            elif complement > 0:
                left += 1
            else:
                left, right = left + 1, right - 1

        return results
