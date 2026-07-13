class Solution:
    ESCAPE = "\\"

    CODE_WORD = r"|"
    SEQUENCE_WORD = ESCAPE + CODE_WORD

    CODE_EMPTY = r"0"
    SEQUENCE_EMPTY = ESCAPE + CODE_EMPTY

    def encode(self, strs: List[str]) -> str:
        escaped = [string.replace(self.SEQUENCE_WORD, self.ESCAPE + self.SEQUENCE_WORD) for string in strs]
        # print(escaped)
        escaped = [string.replace(self.SEQUENCE_EMPTY, self.ESCAPE + self.SEQUENCE_EMPTY) for string in escaped]
        # print(escaped)

        encoded = [self.SEQUENCE_EMPTY if not string else string for string in escaped]
        # print(encoded)
        encoded = self.SEQUENCE_WORD.join(encoded)
        # print(encoded)

        return encoded

    def decode(self, s: str) -> List[str]:
        # print(s)

        result = []
        current = []
        escaped = False

        for char in s:
            if escaped:
                escaped = False

                if char == self.CODE_EMPTY:
                    current = [""]
                    continue

                if char == self.CODE_WORD:
                    result.append("".join(current) if current else "")
                    current = []  # Implied [""].
                    continue

                # Handle additional custom escape sequences here.
                
                # Don't touch non-custom escape sequences.
                current.append(self.ESCAPE + char)
                continue

            if char == self.ESCAPE:
                print("hello")
                escaped = True
                continue

            current.append(char)

        if escaped:
            current.append(self.ESCAPE)

        if current:
            result.append("".join(current))

        return result
