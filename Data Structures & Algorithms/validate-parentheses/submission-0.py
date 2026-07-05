class Solution:
    def isValid(self, s: str) -> bool:
        matching = {

            "}" : "{",
            "]" : "[",
            ")" : "("
        }

        stack = []
        for char in s:
            if char not in matching:
                stack.append(char)
            else:
                if not stack or stack[-1] != matching[char]:
                    return False
                stack.pop()

        return len(stack) == 0
