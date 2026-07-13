class Solution:
    ESCAPE = "\\"
    CODE = r"|"
    SEQUENCE = ESCAPE + CODE

    def encode(self, strs: List[str]) -> str:
        # print(self.ESCAPE)
        # print(self.CODE)
        # print(self.SEQUENCE)

        escaped = [re.sub(self.SEQUENCE, self.ESCAPE + self.SEQUENCE, string) for string in strs]
        encoded = self.SEQUENCE.join(escaped)
        return encoded

    def decode(self, s: str) -> List[str]:
        result = []
        current = []
        escaped = False

        for char in s:
            if escaped:
                escaped = False

                if char == self.CODE:
                    result.append("".join(current))
                    current = []
                    continue

                # Handle additional custom escape sequences here.
                continue

            if char == self.ESCAPE:
                escaped = True
                continue

            current.append(char)

        if current:
            result.append("".join(current))

        return result if result else [""]
