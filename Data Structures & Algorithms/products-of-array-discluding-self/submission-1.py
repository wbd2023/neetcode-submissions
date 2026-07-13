class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixes = []
        suffixes = [1] * len(nums)

        product = 1
        for num in nums:
            product *= num
            prefixes.append(product)

        product = 1
        for index in range(len(nums) - 1, -1, -1):
            product *= nums[index]
            suffixes[index] = product

        result = []

        for index in range(len(nums)):
            prefix = prefixes[index - 1] if index > 0 else 1
            suffix = suffixes[index + 1] if index + 1 < len(nums) else 1
            result.append(prefix * suffix)

        return result
