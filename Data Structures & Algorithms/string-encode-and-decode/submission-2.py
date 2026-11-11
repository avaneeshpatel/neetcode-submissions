class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ''
        for ele in strs:
            s = s+ele+'#%#'
        return s

    def decode(self, s: str) -> List[str]:
        s1 = s.split('#%#')
        return s1[:len(s1)-1]
