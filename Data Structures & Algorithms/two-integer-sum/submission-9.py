class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_dict = {}
        for i in range(len(nums)):
            current = nums[i]
            index_dict[current] = i
        for i in range(len(nums)):
            current = nums[i]
            gap = target-current
            if gap in index_dict and index_dict[gap] != i: 
                index = index_dict[gap]
                return [i,index]
        return []