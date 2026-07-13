class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        values = set(nums)

        for num in values:
            if num - 1 in values:
                continue

            streak = 0
            while num + streak in values:
                streak += 1

            longest = max(longest, streak)

        return longest
