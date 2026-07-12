class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups: Dict[tuple[str, int], List[str]] = defaultdict(list)

        for word in strs:
            digest = Counter(word)
            key = frozenset(digest.items())
            groups[key].append(word)

        return list(groups.values())
