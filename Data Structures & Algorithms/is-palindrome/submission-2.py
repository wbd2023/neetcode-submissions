class Solution:
    def isPalindrome(self, s: str) -> bool:
        normalised = s.lower()
        chars = filter(str.isalnum, normalised)
        processed = "".join(chars)

        i, j = 0, len(processed) - 1
        while i <= j:
            if processed[i] != processed[j]:
                return False

            i += 1
            j -= 1

        return True
