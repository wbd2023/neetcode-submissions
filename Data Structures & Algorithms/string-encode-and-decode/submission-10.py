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
                self.SEQUENCE_WORD,
                self.ESCAPE + self.SEQUENCE_WORD,
            )
            string = string.replace(
                self.SEQUENCE_EMPTY,
                self.ESCAPE + self.SEQUENCE_EMPTY,
            )
            encoded.append(string)

        return self.SEQUENCE_WORD.join(encoded)

    def decode(self, s: str) -> List[str]:
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
                    result.append("".join(current))
                    current = []
                    continue

                # Preserve non-custom escape sequences.
                current.append(self.ESCAPE + char)
                continue

            if char == self.ESCAPE:
                escaped = True
                continue

            current.append(char)

        if escaped:
            current.append(self.ESCAPE)

        if current:
            result.append("".join(current))

        return result
