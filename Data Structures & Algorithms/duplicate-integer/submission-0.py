class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count_dict = {}
        for num in nums:
            if num not in count_dict:
                count_dict[num] = 1
            else:
                return True
        return False
        