class Solution:
    ESCAPE = "\\"
    CODE = r"#"
    SEQUENCE = ESCAPE + CODE

    def encode(self, strs: List[str]) -> str:
        # print(self.ESCAPE)
        # print(self.CODE)
        # print(self.SEQUENCE)
        print(self.ESCAPE + self.SEQUENCE)

        escaped = [re.sub(self.SEQUENCE, self.ESCAPE + self.SEQUENCE, string) for string in strs]
        print(escaped)

        encoded = self.SEQUENCE.join(escaped)
        return encoded

    def decode(self, s: str) -> List[str]:
        print(s)

        result = []
        current = [""]
        escaped = False

        for char in s:
            if escaped:
                escaped = False

                if char == self.CODE:
                    result.append("".join(current) if current else "")
                    current = [""]
                    continue

                # Handle additional custom escape sequences here.
                continue

            if char == self.ESCAPE:
                escaped = True
                continue

            current.append(char)

        if escaped:
            current.append(self.ESCAPE)

        if current:
            result.append("".join(current) if current else "")

        return result
