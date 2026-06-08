class Solution:
    # We want the minimum eating speed `mid` such that the required hours `value` is <= `h`.
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if h < len(piles):
            return sys.maxsize

        low = 1
        high = max(piles)

        best = max(piles)

        while low <= high:
            mid = low + (high - low) // 2

            # Note: `value` and `mid` are inversely proportional.
            value = sum(math.ceil(p / mid) for p in piles)

            if value > h:
                low = mid + 1
                continue

            # If `value` <= `h`.
            high = mid - 1

            if mid < best:
                best = mid

        return best
