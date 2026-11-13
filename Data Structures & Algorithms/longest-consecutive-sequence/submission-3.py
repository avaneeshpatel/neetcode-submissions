class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        num_dict = {}
        for num in nums:
            num_dict[num] = 1
        
        match = 1
        for num in nums:   
            current_match = 1    
            if num-1 not in num_dict:
                current_number = num
                while True:
                    if current_number+1 in num_dict:
                        current_match += 1
                        current_number += 1
                    else:
                        break
            match = max(match,current_match)
        return match


