# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        if len(pairs) <= 1:
            return pairs

        x, y = self.mergeSort(pairs[:len(pairs) // 2]), self.mergeSort(pairs[len(pairs) // 2:])
        i, j = 0, 0
        result = []

        while i < len(x) and j < len(y):
            if x[i].key <= y[j].key:
                result.append(x[i])
                i += 1

            else:
                result.append(y[j])
                j += 1

        result.extend(x[i:])
        result.extend(y[j:])

        return result

    def debug(self, **kwargs) -> None:
        for name, pairs in kwargs.items():
            print(f"{name}: ", end="")
            print([f"({pair.key}, {pair.value})" for pair in pairs])

        print()