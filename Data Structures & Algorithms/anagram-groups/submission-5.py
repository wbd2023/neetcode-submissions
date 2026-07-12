class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for word in strs:
            digest = Counter(word)
            key = frozenset(digest.items())  # Freeze the Counter items to make them hashable (immutable).
            groups[key].append(word)

        return list(groups.values())
