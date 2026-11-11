class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        actual_mul = 1
        actual_mul_without_zero = 0
        zero_count = 0
        for num in nums:
            if num == 0:
                zero_count += 1
            if num != 0:
                if actual_mul_without_zero == 0:
                    actual_mul_without_zero = 1
                
            actual_mul *= num
            if num != 0:
                actual_mul_without_zero *= num
        result = []
        for num in nums:
            if num == 0:
                if zero_count == 1:
                    result.append(actual_mul_without_zero)
                else:
                    result.append(0)
            else:
                result.append(int(actual_mul/num))
        return result
        
        