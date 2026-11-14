class Solution:
    def isPalindrome(self, s: str) -> bool:
        char_dict = {chr(i):0 for i in range(ord('a'),ord('z')+1)}
        for i in range(10):
            char_dict[str(i)] = 1
        
        start = 0
        end = len(s)-1
        while start <= end:
            if s[start].lower() in char_dict and s[end].lower() in char_dict:
                if s[start].lower() == s[end].lower():
                    start += 1
                    end -= 1
                else:
                    return False
            else:
                if s[start].lower() not in char_dict:
                    start += 1
                else:
                    end -=1
        return True
        