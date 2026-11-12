class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        prev = 1
        for num in nums:
            result.append(prev)
            prev = prev*num
        post = 1
        for i in range(len(nums)-1,-1,-1):
            mult = post*result[i]
            result[i] = mult
            post = post*nums[i]
        return result
        
        