class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [set() for _ in range(len(nums))]
        for num in nums:
            for bucket in buckets:
                if num not in bucket:
                    bucket.add(num)
                    break

        results = set()
        for bucket in buckets[::-1]:
            for num in bucket:
                results.add(num)

            if len(results) >= k:
                break

        return list(results)
