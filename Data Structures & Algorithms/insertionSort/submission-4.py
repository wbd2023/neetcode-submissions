# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        if len(pairs) <= 1:
            return [pairs] if pairs else []

        result = []

        for i in range(len(pairs)):
            current = pairs[i]
            j = i - 1

            # Shift pairs behind `current` rightwards, until we find the right place for `current`. 
            while j >= 0 and current.key < pairs[j].key:
                pairs[j + 1] = pairs[j]
                j -= 1

            # Put `current` in the right place.
            pairs[j + 1] = current

            result.append(pairs[:])

        return result
