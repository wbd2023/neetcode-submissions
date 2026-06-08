# We want max value that is smaller than h.
#
# value and mid are inversely proportional


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if h < len(piles):
            return -1

        low = 1
        high = max(piles)

        best = math.inf

        while low <= high:
            mid = low + (high - low) // 2

            value = sum(map(lambda x: math.ceil(x / mid), piles))

            print(f"low={low}, high={high}, mid={mid}, value={value}")

            if value <= h:
                high = mid - 1

                if value >= sum(map(lambda x: math.ceil(x / best), piles)) and mid < best:
                    best = mid

            elif value > h:
                low = mid + 1

        return best
