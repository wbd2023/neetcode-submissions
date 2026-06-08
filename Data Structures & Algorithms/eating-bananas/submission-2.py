# We want max value that is smaller than h.
#
# value and mid are inversely proportional


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if h < len(piles):
            return int(math.inf)

        low = 1
        high = max(piles)

        best = max(piles)

        while low <= high:
            mid = low + (high - low) // 2

            value = sum(map(lambda x: math.ceil(x / mid), piles))

            print(f"low={low}, high={high}, mid={mid}, value={value}")

            if value > h:
                low = mid + 1

            else:  # value <= h
                high = mid - 1

                if mid < best and value >= sum(map(lambda x: math.ceil(x / best), piles)):
                    best = mid

        return best
