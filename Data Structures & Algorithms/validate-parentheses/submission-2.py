class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map = {
            "(" : ")",
            "{" : "}",
            "[" : "]"
        }

        stack = []

        for char in s:
            if char in bracket_map:
                stack.append(char)
            else:
                if not stack:
                    return False
                last_char= stack.pop()
                if bracket_map[last_char] != char:
                    return False
        
        return not stack


        