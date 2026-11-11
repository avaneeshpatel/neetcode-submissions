class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = {}
        for num in nums:
            count_dict[num] = count_dict.get(num,0)+1
        count_arr = [None]*(len(nums)+1)
        for key in count_dict.keys():
            value = count_dict[key]
            if count_arr[value] == None:
                count_arr[value] = [key]
            else:
                count_arr[value] += [key]
        
        index = len(count_arr)-1
        result = []
        while index >= 0 and k > 0: 
            if count_arr[index] == None:
                index -= 1
                continue
            current_element = count_arr[index]
            result += current_element
            k -= len(current_element)
            index -= 1
        return result
        