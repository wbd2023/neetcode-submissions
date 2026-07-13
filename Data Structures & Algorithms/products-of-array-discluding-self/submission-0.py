class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_products = []
        suffix_products = [1] * len(nums)

        product = 1
        for num in nums:
            product *= num
            prefix_products.append(product)

        product = 1
        for index in range(len(nums) - 1, -1, -1):
            product *= nums[index]
            suffix_products[index] = product

        result = []

        for index in range(len(nums)):
            prefix = prefix_products[index - 1] if index > 0 else 1
            suffix = suffix_products[index + 1] if index + 1 < len(nums) else 1
            result.append(prefix * suffix)

        return result
