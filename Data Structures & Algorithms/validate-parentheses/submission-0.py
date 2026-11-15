class Solution:
    def isValid(self, s: str) -> bool:
        outer_characters = (')',']','}')
        inner_characters = ('(','{','[')
        character_dict = {'}':'{',")":"(","]":"["}
        stack = []
        for i in range(len(s)):
            if s[i] in inner_characters:
                stack.append(s[i])
            else:
                if len(stack) == 0 or stack[-1] != character_dict[s[i]]:
                    return False
                else:
                    stack.pop(-1)
        if len(stack) == 0:
            return True
        return False
        