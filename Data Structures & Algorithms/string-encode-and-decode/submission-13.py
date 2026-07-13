class Solution:
    ESCAPE = "\\"

    CODE_WORD = "|"
    SEQUENCE_WORD = ESCAPE + CODE_WORD

    CODE_EMPTY = "0"
    SEQUENCE_EMPTY = ESCAPE + CODE_EMPTY

    def encode(self, strs: List[str]) -> str:
        encoded = []

        for string in strs:
            if not string:
                encoded.append(self.SEQUENCE_EMPTY)
                continue

            string = string.replace(
                self.ESCAPE,
                self.ESCAPE + self.ESCAPE,
            )

            encoded.append(string)

        return self.SEQUENCE_WORD.join(encoded)

    def decode(self, s: str) -> List[str]:
        result = []
        current = []
        escaped = False

        for char in s:
            if not escaped:
                if char == self.ESCAPE:
                    escaped = True
                    continue

                current.append(char)
                continue

            escaped = False

            if char == self.ESCAPE:
                current.append(self.ESCAPE)
                continue

            if char == self.CODE_EMPTY:
                current = [""]
                continue

            if char == self.CODE_WORD:
                result.append("".join(current))
                current = []
                continue

            # Preserve non-custom escape sequences.
            current.append(self.ESCAPE + char)

        if escaped:
            current.append(self.ESCAPE)

        if current:
            result.append("".join(current))

        return result
