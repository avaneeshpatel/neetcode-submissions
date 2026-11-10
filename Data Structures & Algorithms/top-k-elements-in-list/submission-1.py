class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = {}
        for num in nums:
            count_dict[num] = count_dict.get(num,0)+1
        result = []
        values = list(count_dict.values())
        values.sort(reverse=True)
        consider_values = values[:k]
        consider_values_dict = {}
        for ele in consider_values:
            consider_values_dict[ele]=1
        for key in count_dict.keys():
            if count_dict[key] in consider_values_dict:
                result.append(key)
        return result
        