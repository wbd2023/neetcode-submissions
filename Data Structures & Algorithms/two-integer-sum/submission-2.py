class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complements = {}

        for index, num in enumerate(nums):
            complement = target - num

            if num in complements.keys():
                return [complements[num], index]

            complements[complement] = index

        raise ValueError("Assume a valid answer exists.")
