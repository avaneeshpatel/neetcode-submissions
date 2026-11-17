class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            current = nums[i]
            start = i+1
            end = len(nums)-1
            while start < end:
                sum1 = current + nums[start]+nums[end]
                if sum1 == 0:
                    result.append([current,nums[start],nums[end]])
                    start += 1
                    end -=1
                    while start < end and nums[start] == nums[start-1]:
                        start += 1
                    while start < end and nums[end] == nums[end+1]:
                        end -=1
                elif sum1 < 0:
                    start += 1
                else:
                    end -= 1
        return result
                    
                    

        