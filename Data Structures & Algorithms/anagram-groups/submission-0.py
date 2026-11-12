class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = {}
        for word in strs:
            char_count = {chr(i):0 for i in range(ord('a'),ord('z')+1)}
            for char in word:
                char_count[char] = char_count[char]+1
            char_count = str(char_count)
            anagram_dict[char_count] = anagram_dict.get(char_count,[])+[word]
        result = []
        for key in anagram_dict.keys():
            result.append(anagram_dict[key])
        return result
        