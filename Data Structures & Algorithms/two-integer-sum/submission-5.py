class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_dict = {}
        for i in range(len(nums)):
            current = nums[i]
            index_dict[current] = index_dict.get(current,[])+[i]
        for i in range(len(nums)):
            current = nums[i]
            gap = target-current
            if gap in index_dict:
                
                index_0 = index_dict[gap][0]
                if index_0 != i:
                    return [i,index_0]
                else:
                    if len(index_dict[gap])>1:
                        index_1 = index_dict[gap][1]
                        return [i,index_1]